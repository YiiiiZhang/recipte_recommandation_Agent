from dataclasses import dataclass
import os


@dataclass
class Settings:
    model_path: str = os.getenv(
        "MODEL_PATH",
        "/dss/dssmcmlfs01/pn25ju/pn25ju-dss-0000/models/Qwen2.5-7B-Instruct",
    )
    device_map: str = os.getenv("DEVICE_MAP", "auto")
    max_new_tokens: int = int(os.getenv("MAX_NEW_TOKENS", "256"))
    temperature: float = float(os.getenv("TEMPERATURE", "0.2"))
    do_sample: bool = os.getenv("DO_SAMPLE", "false").lower() == "true"


settings = Settings()