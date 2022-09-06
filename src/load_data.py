"""Load posts from VK and store its."""
import requests
import pandas as pd
from datetime import datetime
from pathlib import Path
from loguru import logger

from src import configurations
from src.schemas import PostInfo, PostInfoList, SocialGroupInfo


POST_NUMBER = 100000


def get_group_info(group_name: str) -> SocialGroupInfo:
    """Выдача информации о группе."""
    logger.info(f"Send GET-request about group {group_name}")
    response = requests.get(url=configurations.VK_API_URL.format(method="groups.getById"),
                            params={
                               "v": configurations.VK_API_VERSION,
                               "access_token": configurations.ACCESS_TOKEN,
                               "group_ids": group_name,
                               "fields": "description",
                           })
    logger.info(f"Response has status {response.status_code}")
    data = response.json()["response"][0]
    return SocialGroupInfo(**data)


def store_post_data(group_id: int, post_number: int = POST_NUMBER, post_batch_size: int = 100) -> None:
    """Сохранение информации о постах в CSV-файл."""
    logger.info(f"Start storing posts...")

    posts = PostInfoList(items=[])
    offset = 0

    while offset < post_number:
        response_post_info = requests.post(url=configurations.VK_API_URL.format(method="wall.get"),
                                           params={
                                              "v": configurations.VK_API_VERSION,
                                              "access_token": configurations.ACCESS_TOKEN,
                                              "owner_id": -group_id,
                                              "count": post_batch_size,
                                              "offset": offset,
                                           })

        if response_post_info.status_code != 200:
            logger.error(f"Response with status: {response_post_info.status_code}, "
                         f"description: {response_post_info.text}")
            break

        try:
            posts.items.extend([PostInfo(id=item["id"], text=item["text"], likes=item["likes"]["count"],
                                         views=item["views"]["count"], reposts=item["reposts"]["count"])
                                for item in response_post_info.json()["response"]["items"]])
            if offset == len(posts.items):
                break
        except KeyError:
            continue
        finally:
            offset = len(posts.items)
            logger.debug(f"Loaded posts: {len(posts.items)}")

    data = posts.dict()["items"]
    posts_df = pd.DataFrame(data=data)
    time_now = datetime.now()
    file_path = Path(configurations.POST_DATASET_PATH
                     / f"posts_{time_now.strftime('%d_%m_%Y_%H_%M_%S')}.csv").as_posix()
    posts_df.to_csv(file_path, index=False)
    logger.info(f"Posts successfully stored in {file_path}")


if __name__ == "__main__":
    group_info = get_group_info(input("Название группы в ВК: "))
    store_post_data(group_info.id)
