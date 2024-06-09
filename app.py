from raducord import Console, Logger
from colorama import Fore, Back, Style
import instaloader
from concurrent.futures import ThreadPoolExecutor
import json
import time
import os

Console.init()

config = json.load(open("config.json"))

"""
discord me : thee0x91
"""

class InstagramTool:
    @staticmethod
    def codemenu():
        os.system('cls')
        print(f"""
                                                                                 \033[31minstagram tool\033[0m by \033[36mthee0x91\033[0m
              

{Fore.LIGHTCYAN_EX}                                    ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗    ████████╗ ██████╗  ██████╗ ██╗     {Fore.RESET}
{Fore.LIGHTCYAN_EX}                                    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     {Fore.RESET}
{Fore.LIGHTCYAN_EX}                                    ██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║       ██║   ██║   ██║██║   ██║██║     {Fore.RESET}
{Fore.LIGHTCYAN_EX}                                    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║     {Fore.RESET}
{Fore.LIGHTCYAN_EX}                                    ██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗{Fore.RESET}
{Fore.LIGHTCYAN_EX}                                    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝{Fore.RESET}
                                                                                                                 
        """)

        print(f"""
{Fore.BLUE}{Back.BLACK}
                                                                                ╔════════════════════════════════╗
                                                                                ║                                ║
                                                                                ║    1. Storyloader              ║
                                                                                ║                                ║
                                                                                ║    2. Check Following          ║
                                                                                ║                                ║
                                                                                ╚════════════════════════════════╝
{Style.RESET_ALL}
        """)

        choice = input(f"{Fore.GREEN}Please select an option (1 or 2): {Fore.RESET}")

        if choice == '1':
            InstagramTool.Storyloader()
        elif choice == '2':
            InstagramTool.checkfollowing()
        else:
            print(f"{Fore.RED}Invalid option. Please select 1 or 2.{Fore.RESET}")
            InstagramTool.codemenu()

    @staticmethod
    def Storyloader():
        L = instaloader.Instaloader()

        username = config["USERNAME"]
        password = config["PASSWORD"]

        L.login(username, password)

        target_username = input(f"{Fore.GREEN}Enter the target username: {Fore.RESET}")

        download_posts = input(f"{Fore.GREEN}Download posts? (y/n): {Fore.RESET}").lower() == 'y'
        download_highlights = input(f"{Fore.GREEN}Download highlights? (y/n): {Fore.RESET}").lower() == 'y'
        download_stories = input(f"{Fore.GREEN}Download stories? (y/n): {Fore.RESET}").lower() == 'y'

        log_filename = f"log/Storyloader/{target_username}.txt"
        os.makedirs(os.path.dirname(log_filename), exist_ok=True)

        with open(log_filename, 'w') as log_file:
            def log(msg):
                print(msg)
                log_file.write(msg + '\n')

            def download_storyitem(item, target):
                try:
                    L.download_storyitem(item, target=target)
                    log(f"Downloaded story item {item} to {target}")
                except Exception as e:
                    log(f"Error downloading story item: {e}")

            def download_post(post, target):
                try:
                    L.download_post(post, target=target)
                    log(f"Downloaded post {post} to {target}")
                except Exception as e:
                    log(f"Error downloading post: {e}")

            def download_stories(target_username):
                profile = instaloader.Profile.from_username(L.context, target_username)
                with ThreadPoolExecutor() as executor:
                    for story in L.get_stories(userids=[profile.userid]):
                        executor.map(lambda item: download_storyitem(item, target=profile.username), story.get_items())

            def download_highlights(target_username):
                profile = instaloader.Profile.from_username(L.context, target_username)
                with ThreadPoolExecutor() as executor:
                    for highlight in L.get_highlights(profile):
                        executor.map(lambda item: download_storyitem(item, target=f"{profile.username}_highlights"), highlight.get_items())

            def download_posts(target_username):
                profile = instaloader.Profile.from_username(L.context, target_username)
                with ThreadPoolExecutor() as executor:
                    executor.map(lambda post: download_post(post, target=f"{profile.username}_posts"), profile.get_posts())

            if download_stories:
                download_stories(target_username)
            if download_highlights:
                download_highlights(target_username)
            if download_posts:
                download_posts(target_username)

            log(f"Success! Download completed for {target_username}.")
            Logger.success(f"Success Dowload,Instagram tool,{target_username}")

        time.sleep(2)
        InstagramTool.codemenu()

    @staticmethod
    def checkfollowing():
        L = instaloader.Instaloader()

        username = config["USERNAME"]
        password = config["PASSWORD"]

        L.login(username, password)

        target_username = input(f"{Fore.GREEN}Enter the target username to check: {Fore.RESET}")

        log_filename = f"log/checkfollowing/{target_username}.txt"
        os.makedirs(os.path.dirname(log_filename), exist_ok=True)

        with open(log_filename, 'w') as log_file:
            def log(msg):
                print(msg)
                log_file.write(msg + '\n')

            profile = instaloader.Profile.from_username(L.context, target_username)

            following = set(profile.get_followees())
            followers = set(profile.get_followers())

            not_following_back = following - followers

            for user in not_following_back:
                log(user.username)

            log(f"Success! Checked following for {target_username}.")
            Logger.success(f"Success Check,Instagram tool,{target_username}")

        time.sleep(2)
        InstagramTool.codemenu()

main = InstagramTool
main.codemenu()
