"""
Module for user status update
"""
import os
import requests
import json
from graphqlclient import GraphQLClient

def get_user_token():
    """
    Prompt the user to give login info 
    """
    token = input("Github account access token (if you don't have one please visit https://github.com/settings/tokens) : ")

    username = input("Github account username : ")

    return token, username


def mutate_user_status(username: str, token: str):
    message = input("What message should your github status display ? (default : Drinking tea under the stars) : ") or "Drinking Tea under the stars"
    emoji = input("What emoji should you set for your user status ? default set to :tea: (for a complete list, you can visit https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia ) : ") or ":tea:"

    client = GraphQLClient("https://api.github.com/graphql")
    client.inject_token("Bearer " + token)

    variables = {'name': username , 'icon': emoji, 'status': message}

    query = '''
        mutation changeUserStatus($name: String!, $icon: String!, $status: String!){
                changeUserStatus(input: {clientMutationId: $name, emoji: $icon, message: $status}) {
                            clientMutationId
                            status {
                                message
                                emoji
                            }
                    }    
                }

'''

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
    
