from hydra import main
from omegaconf import DictConfig

from pipeline.pipeline import Pipeline


@main(config_path="../conf", config_name="config", version_base="1.2")
def run(cfg: DictConfig):
    pipeline = Pipeline(cfg)
    pipeline.run()


if __name__ == "__main__":
    run()
