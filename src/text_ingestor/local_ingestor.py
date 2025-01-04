class LocalIngestor:
    """
    Access local text files (i.e. *.txt) to ingest text for the pipeline
    """

    def __init__(self):
        pass

    def run(self, filepath: str) -> None:
        # Open and read the entire file
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        return content
