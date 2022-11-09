# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 13:48:47 2022

@author: fierz
"""

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playergamelog, teamgamelog

player_dict = players.get_players()
player_input = "Stephen Curry"
season_input = "2019"
this_player = [player for player in player_dict if player['full_name'] == player_input][0]
this_id = this_player['id']
player_gamelog = playergamelog.PlayerGameLog(player_id = this_id, season = season_input)
player_gamelog_df = player_gamelog.get_data_frames()[0]


team_dict = teams.get_teams()
team_input = "CLE"
season_input = "2020"
this_team = [team for team in team_dict if team['abbreviation'] == team_input][0]
this_id = this_team['id']
team_gamelog = teamgamelog.TeamGameLog(team_id = this_id, season = season_input)
team_gamelog_df = team_gamelog.get_data_frames()[0]
