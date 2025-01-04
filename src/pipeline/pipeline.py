from text_ingestor.local_ingestor import LocalIngestor
from topic_extractor.topic_extractor import TopicExtractor


class Pipeline:
    """
    Orchestrate stages of pipeline
    """

    def __init__(self, cfg):
        self.config = cfg

    def run(self):
        """
        Run various stages of pipeline
        """

        # Text Ingestion
        local_filepath = "data/raw_texts/ai_agent_1.txt"
        local_ingestor = LocalIngestor()
        text = local_ingestor.run(local_filepath)

        # Doc-level topic extraction
        topic_extractor = TopicExtractor(self.config)
        output = topic_extractor.run(text)
        print(output)
