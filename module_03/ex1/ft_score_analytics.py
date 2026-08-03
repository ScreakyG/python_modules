#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    if (len(sys.argv) <= 1):
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    
    scores_args = sys.argv[1:]
    score_list: list[int] = []

    # Parse args into int list
    for score in scores_args:
        try:
            score_list.append(int(score))            
        except ValueError:
            print(f"Invalid parameter: '{score}'")

    # If no item parsed exit
    if len(score_list) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    # Display scores stats if items in list
    print(f"Scores processed: {score_list}")
    print("Total players:", len(score_list))
    print("Total score:", sum(score_list))
    print("Average score:", sum(score_list) / len(score_list))
    print("High score:", max(score_list))
    print("Low score:", min(score_list))
    print("Score range:", max(score_list) - min(score_list))

if __name__ == '__main__':
    main()
