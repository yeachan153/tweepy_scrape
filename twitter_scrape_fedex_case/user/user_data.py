from twitter_scraper import Profile


def get_user_data(username: str) -> dict:
    """Gets user data.

    Args:
        username (str): username of tweet.

    Returns:
        dict: dictionary containing user info.
    """
    profile = Profile(username=username)
    return profile.to_dict()
