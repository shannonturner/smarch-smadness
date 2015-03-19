import random

with open("7.txt") as teams_file:
    teams = teams_file.read().strip().split("\n")

def round_winners(teams=[]):
    advancing = []
    for index, team in list(enumerate(teams))[::2]:
        print '{0} vs {1}'.format(teams[index],teams[index+1])
        winner = random.choice([teams[index], teams[index+1]])
        print "\t", winner
        advancing.append(winner)
    return advancing

# rounds = [16, 8]
# rounds = [8, 4]
rounds = [4, 2]

for index, team_count in enumerate(rounds):
    assert len(teams) == team_count
    print "[INFO] Round {0} ({1} teams)".format(index, team_count)
    advancing = round_winners(teams)
    teams = list(advancing)
    print "Advancing to the next round: "
    print "\t\t", teams

# Calculate tiebreaker final score
winning_scores = []
losing_scores = []

with open("final_scores.txt") as final_scores_file:
    final_scores = final_scores_file.read().strip().split("\n")
    for final_score in final_scores:
        winning_score, losing_score = final_score.split("\t")
        winning_scores.append(int(winning_score))
        losing_scores.append(int(losing_score))

print sum(winning_scores) / float(len(winning_scores))
print sum(losing_scores) / float(len(losing_scores))

