from typing import List, Dict

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from app.config import settings
from app.llm.base import BaseLLM
from app.utils.logger import get_logger


logger = get_logger(__name__)


class LocalQwenLLM(BaseLLM):
    def __init__(self, model_path: str | None = None):
        self.model_path = model_path or settings.model_path
        logger.info("Loading tokenizer from %s", self.model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)

        logger.info("Loading model from %s", self.model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_path,
            torch_dtype="auto",
            device_map=settings.device_map,
        )
        self.model.eval()
        logger.info("Model loaded successfully.")

    def chat(self, messages: List[Dict[str, str]]) -> str:
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )

        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            generated_ids = self.model.generate(
                **model_inputs,
                max_new_tokens=settings.max_new_tokens,
                do_sample=settings.do_sample,
            )

        generated_ids = [
            output_ids[len(input_ids):]
            for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(
            generated_ids,
            skip_special_tokens=True,
        )[0]

        return response.strip()