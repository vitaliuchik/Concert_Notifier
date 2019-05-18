"""
Previous loginnig in Google Play Music account
"""
from gmusicapi import Mobileclient

if __name__ == '__main__':
    api = Mobileclient()
    api.perform_oauth()