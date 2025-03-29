from rest_framework import serializers
from .models import Box, BoxKey, Bracket, League, LeagueTournament, LegacyBracket, Team, Tournament, UserLeague, User

class BoxSerializer(serializers.ModelSerializer):
  class Meta:
    model = Box
    fields = ['bracket_id', 'team_id', 'code']

class BoxKeySerializer(serializers.ModelSerializer):
  class Meta:
    model = BoxKey
    fields = ['tournament_id', 'team_id', 'code']

class BracketSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bracket
    fields = ['name', 'user_id', 'points', 'league_tournament_id', 'content']

class LeagueSerializer(serializers.ModelSerializer):
  class Meta:
    model = League
    fields = ['name', 'password', 'admin_id', 'brackets', 'users', 'legacy_brackets', 'tournaments']

class LeagueTournamentSerializer(serializers.ModelSerializer):
  class Meta:
    model = LeagueTournament
    fields = ['league_id', 'tournament_id', 'brackets_per_user']

class LegacyBracketSerializer(serializers.ModelSerializer):
  class Meta:
    model = LegacyBracket
    fields = ['user_id', 'league_tournament_id', 'champion_id', 'points']

class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Team
    fields = ['school', 'nickname', 'abbreviation', 'logo_url', 'color_primary_hex', 'color_secondary_hex']

class TournamentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tournament
    fields = ['name', 'submission_open', 'start_date', 'end_date', 'key_type', 'max_points', 'key']

class UserLeagueSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserLeague
    fields = ['user_id', 'league_id', 'joined_on', 'retired_on']

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'password', 'joined_on', 'system_admin', 'brackets', 'legacy_brackets', 'leagues']
