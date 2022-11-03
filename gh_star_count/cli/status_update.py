"""
Module for user status update
"""
from graphqlclient import GraphQLClient  # type: ignore


def get_user_token():
    """
    Prompt the user to give login info
    """
    token_prompt_message = (
        "Github account access token "
        "(don't have one ? please visit https://github.com/settings/tokens) : "
    )

    token = input(token_prompt_message)

    username = input("Github account username : ")

    return token, username


def mutate_user_status(username: str, token: str):
    """
    GraphQL mutation query: prompt for information to change and return
    query response

    args:
        username: str
        token: str
    """
    user_status_message_prompt = (
        "What message should your github status display ?"
        " (default : I'm a star!) : "
    )

    message = input(user_status_message_prompt) or "I'm a star!"

    emoji = (
        input(
            (
                "What emoji should you set for your user status ?"
                " default ':sunglasses:'"
                "(for a complete list, you can visit: "
                "https://dev.to/nikolab/complete-list-of-github-markdown"
                "-emoji-markup-5aia ): "
            )
        )
        or ":sunglasses:"
    )

    client = GraphQLClient("https://api.github.com/graphql")
    client.inject_token("Bearer " + token)

    variables = {"name": username, "icon": emoji, "status": message}

    query = """
        mutation changeUserStatus(
        $name: String!, $icon: String!, $status: String!
        )
        {changeUserStatus(
            input: {clientMutationId: $name, emoji: $icon, message: $status})
            {
                        clientMutationId
                        status {
                                message
                                emoji
                               }
                }
        }
    """

    result = client.execute(query, variables)

    return result


def main_status_update():
    """
    Main function for updating user status on Github
    """
    token, name = get_user_token()
    result = mutate_user_status(name, token)
    return result


if __name__ == "__main__":
    main_status_update()
