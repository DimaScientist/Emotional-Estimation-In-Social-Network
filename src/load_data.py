"""Load posts from VK and store its."""
from src.elastic import Elastic


if __name__ == "__main__":
    elastic = Elastic()
    print(elastic.info())
