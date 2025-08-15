#!/usr/bin/env python3
"""
Testing and Validation Framework for Syracuse Women's Lacrosse 2024 Statistics
Framework for systematic evaluation of LLM performance on sports analytics
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime
from typing import Dict, List, Tuple, Any
import logging
import re


class ResultsAnalyzer:
    """Analyze and summarize LLM testing results"""

    def __init__(self):
        self.results = []

    def add_result(self, prompt_type: str, question: str, llm_response: str,
                   validation_result: Dict[str, Any]):
        """Add a test result"""
        self.results.append({
            'timestamp': datetime.now().isoformat(),
            'prompt_type': prompt_type,
            'question': question,
            'llm_response': llm_response,
            'validation': validation_result
        })

    def generate_summary_report(self) -> str:
        """Generate comprehensive summary report"""
        if not self.results:
            return "No results to analyze."

        # Calculate success rates by type
        type_stats = {}
        for result in self.results:
            ptype = result['prompt_type']
            if ptype not in type_stats:
                type_stats[ptype] = {'total': 0, 'accurate': 0}

            type_stats[ptype]['total'] += 1
            if result['validation'].get('accuracy', False):
                type_stats[ptype]['accurate'] += 1

        report = "# LLM Testing Summary Report\n\n"
        report += f"**Total Tests Conducted:** {len(self.results)}\n"
        report += f"**Test Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n"

        report += "## Success Rates by Question Type\n\n"
        for ptype, stats in type_stats.items():
            success_rate = (stats['accurate'] / stats['total']
                            ) * 100 if stats['total'] else 0.0
            report += f"- **{ptype.title()}**: {success_rate:.1f}% ({stats['accurate']}/{stats['total']})\n"

        report += "\n## Key Findings\n\n"

        # Identify patterns
        accurate_results = [
            r for r in self.results if r['validation'].get('accuracy', False)]
        inaccurate_results = [
            r for r in self.results if not r['validation'].get('accuracy', False)]

        if accurate_results:
            report += "### Successful Patterns\n"
            for result in accurate_results[:3]:  # Top 3 examples
                report += f"- {result['question']}: Success\n"

        if inaccurate_results:
            report += "\n### Common Errors\n"
            error_types = {}
            for result in inaccurate_results:
                error_type = result['validation'].get('error_type', 'unknown')
                error_types[error_type] = error_types.get(error_type, 0) + 1

            for error, count in error_types.items():
                report += f"- {error.replace('_', ' ').title()}: {count} occurrences\n"

        return report

    def export_results(self, filename: str):
        """Export results to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"Results exported to {filename}")


def create_syracuse_2024_dataset():
    """Create Syracuse Women's Lacrosse 2024 dataset from official statistics"""

    # Syracuse Women's Lacrosse 2024 Player Statistics
    # Data collected from official team scorebook
    syracuse_players = {
        'Player': [
            'Meaghan Tyrrell', 'Olivia Adamson', 'Emma Ward', 'Sam Swart',
            'Payton Rowley', 'Maddy Baxter', 'Savannah Sweitzer', 'Emma Madnick',
            'Jody Cerullo', 'Grace Britton', 'Kendall Rose', 'Kaci Benoit',
            'Sloane Clark', 'Katie Goodale', 'Mackenzie Rich', 'Victoria Reid',
            'Ryann Banks', 'Hallie Simpkins', 'McKenzie Oleen', 'Ruby Hnatkowiak',
            'Sydney Pirreca', 'Carlie Desimone', 'Ally Quirk', 'Tate Paulson',
            'Ryan Johnson', 'Georgia Sexton-Stone', 'Gwenna Gento', 'Ezra Lahan',
            'Ella Bree', 'Talia Waders', 'Jenna Marino', 'Ana Horvit',
            'Delaney Swartout', 'Daniella Guyette'
        ],
        'Jersey': [
            22, 22, 23, 2, 19, 22, 21, 22,
            17, 19, 7, 22, 9, 31, 10, 7,
            4, 22, 21, 22, 6, 9, 5, 1,
            6, 7, 7, 7, 6, 5, 3, 7,
            22, 7
        ],
        'Goals': [
            70, 58, 44, 29, 23, 30, 24, 14,
            11, 6, 8, 1, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0
        ],
        'Assists': [
            32, 25, 37, 18, 15, 6, 9, 13,
            3, 4, 1, 0, 0, 1, 1, 0,
            1, 1, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0
        ],
        'Points': [
            102, 83, 81, 47, 38, 36, 33, 27,
            14, 10, 9, 1, 1, 1, 1, 0,
            1, 1, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0
        ],
        'Shots': [
            115, 109, 90, 53, 55, 64, 54, 42,
            29, 17, 11, 3, 1, 2, 1, 2,
            1, 0, 4, 2, 1, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0
        ],
        'Games_Played': [
            21, 12, 10, 19, 15, 14, 8, 15,
            10, 3, 3, 21, 1, 43, 19, 19,
            0, 26, 3, 1, 10, 0, 0, 1,
            0, 0, 0, 1, 1, 0, 0, 0,
            4, 0
        ]
    }

    # Create DataFrame
    df = pd.DataFrame(syracuse_players)

    # Calculate additional statistics
    df['Shooting_Pct'] = np.where(
        df['Shots'] > 0, (df['Goals'] / df['Shots']) * 100, 0.0)
    df['Goals_Per_Game'] = np.where(
        df['Games_Played'] > 0, df['Goals'] / df['Games_Played'], 0.0)
    df['Points_Per_Game'] = np.where(
        df['Games_Played'] > 0, df['Points'] / df['Games_Played'], 0.0)

    # Derive team-level statistics from the DataFrame to avoid mismatch
    total_goals = int(df['Goals'].sum())
    total_assists = int(df['Assists'].sum())

    team_stats = {
        'season_record': '16-6',
        'total_games': 22,
        'home_record': '9-2',
        'away_record': '5-2',
        'neutral_record': '2-2',
        'conference_record': '9-1',
        'non_conference_record': '7-5',
        'total_team_goals': total_goals,     # derived
        'total_team_assists': total_assists,  # derived
        'team_shots': int(df['Shots'].sum()),
        'team_shot_pct': round((total_goals / max(1, int(df['Shots'].sum()))) * 100, 2) if int(df['Shots'].sum()) > 0 else 0,
        # keep these as placeholders if you need them; otherwise compute properly from game logs
        'goals_per_game': None,
        'goals_against_per_game': None
    }

    return df, team_stats


class SyracuseDataValidator:
    """Validates LLM responses against real Syracuse Women's Lacrosse 2024 statistics"""

    def __init__(self):
        """Initialize with real Syracuse 2024 data"""
        self.df, self.team_stats = create_syracuse_2024_dataset()
        self.ground_truth = self._calculate_ground_truth()

        # Save the dataset for reference
        self.df.to_csv('syracuse_lacrosse_2024_real.csv', index=False)
        print("Syracuse 2024 data saved to syracuse_lacrosse_2024_real.csv")

    def _calculate_ground_truth(self) -> Dict[str, Any]:
        """Calculate known statistics from Syracuse data for validation"""
        stats = {}

        # Team-level statistics
        stats['total_games'] = self.team_stats['total_games']
        stats['season_record'] = self.team_stats['season_record']
        stats['wins'] = 16
        stats['losses'] = 6

        # Top performers
        stats['top_scorer'] = self.df.loc[self.df['Goals'].idxmax(), 'Player']
        stats['top_scorer_goals'] = int(self.df['Goals'].max())

        stats['top_assist'] = self.df.loc[self.df['Assists'].idxmax(),
                                          'Player']
        stats['top_assist_count'] = int(self.df['Assists'].max())

        stats['top_points'] = self.df.loc[self.df['Points'].idxmax(), 'Player']
        stats['top_points_count'] = int(self.df['Points'].max())

        # Team totals
        stats['total_goals'] = int(self.df['Goals'].sum())
        stats['total_assists'] = int(self.df['Assists'].sum())
        stats['total_points'] = int(self.df['Points'].sum())

        # Shooting statistics (minimum 10 shots for qualification)
        qualified_shooters = self.df[self.df['Shots'] >= 10].copy()
        if not qualified_shooters.empty:
            best_shooter_idx = qualified_shooters['Shooting_Pct'].idxmax()
            stats['best_shooter'] = str(
                qualified_shooters.loc[best_shooter_idx, 'Player'])
            stats['best_shooting_pct'] = float(
                qualified_shooters.loc[best_shooter_idx, 'Shooting_Pct'])

        # Active scorers (players with at least 5 goals)
        stats['active_scorers'] = int((self.df['Goals'] >= 5).sum())

        # Intermediate ground truth
        top3 = self.df.sort_values('Goals', ascending=False).head(3).copy()
        top3['Shooting_Pct_calc'] = np.where(
            top3['Shots'] > 0, (top3['Goals'] / top3['Shots']) * 100.0, 0.0
        )
        stats['top3_shooting'] = [
            {
                'player': str(row['Player']),
                'shooting_pct': round(float(row['Shooting_Pct_calc']), 1)
            }
            for _, row in top3.iterrows()
        ]
        stats['count_ge_10_goals'] = int((self.df['Goals'] >= 10).sum())

        return stats

    def get_testing_context(self) -> str:
        """Get formatted data context for LLM testing"""
        context = f"""
Syracuse Women's Lacrosse 2024 Season Statistics:

TEAM RECORD: {self.team_stats['season_record']} ({self.team_stats['total_games']} games)
- Home: {self.team_stats['home_record']}
- Away: {self.team_stats['away_record']}  
- Conference: {self.team_stats['conference_record']}

TOP PERFORMERS:
"""

        # Get top 10 scorers for context
        top_scorers = self.df.nlargest(
            10, 'Goals')[['Player', 'Goals', 'Assists', 'Points', 'Shots', 'Games_Played']]

        for _, player in top_scorers.iterrows():
            if player['Goals'] > 0:  # Only include actual contributors
                shooting_pct = (
                    player['Goals'] / player['Shots'] * 100.0) if player['Shots'] > 0 else 0.0
                context += f"- {player['Player']}: {int(player['Goals'])}G, {int(player['Assists'])}A, {int(player['Points'])}Pts, {int(player['Shots'])} shots ({shooting_pct:.1f}%)\n"

        # Always use DataFrame-derived totals to avoid mismatch
        team_goals = int(self.df['Goals'].sum())
        team_assists = int(self.df['Assists'].sum())
        context += f"\nTEAM TOTALS: {team_goals} Goals, {team_assists} Assists"

        return context

    # ---------- NEW HELPERS FOR PART 2 ----------
    def _extract_numbers_and_percents(self, text: str) -> Tuple[List[float], List[float]]:
        """Extract numeric values (ints/decimals) and percentages from text."""
        # integers and decimals
        nums = re.findall(r'\b\d+(?:\.\d+)?\b', text)
        # tokens like "60.9%" or "60.9 %"
        pcts = re.findall(r'\b\d+(?:\.\d+)?\s*%', text)
        pct_vals = [float(p.rstrip('%').strip()) for p in pcts]
        vals = [float(n) for n in nums]
        return vals, pct_vals

    def _score_strategic_response(self, text: str) -> Dict[str, int]:
        """Score a free-form strategic response using a simple rubric."""
        text_l = text.lower()

        # Specificity: mentions real players and numbers
        names = [str(n).lower()
                 for n in self.df['Player'].tolist() if str(n).strip()]
        mentions = sum(1 for n in names if n in text_l)
        contains_numbers = bool(re.search(r'\d', text_l))
        specificity = 1 + min(4, mentions // 2) + \
            (1 if contains_numbers else 0)
        specificity = min(5, specificity)

        # Actionability: presence of concrete coaching verbs/ideas
        action_terms = [
            'focus', 'improve', 'increase', 'reduce', 'practice', 'drill', 'scheme',
            'set play', 'assign', 'rotate', 'substitute', 'optimize', 'work on',
            'emphasize', 'target', 'adjust', 'press', 'zone', 'man-to-man', 'transition'
        ]
        actionability = 1 + sum(1 for t in action_terms if t in text_l)
        actionability = max(1, min(5, actionability))

        # Plausibility: no contradictions to key stats (e.g., wrong top scorer)
        plausible = True
        top_scorer = str(self.ground_truth['top_scorer']).lower()
        # If they explicitly claim a different top scorer, penalize
        if ('top scorer' in text_l or 'leading scorer' in text_l) and (top_scorer not in text_l):
            plausible = False
        plausibility = 5 if plausible else 2

        return {'specificity': specificity, 'actionability': actionability, 'plausibility': plausibility}
    # -------------------------------------------

    def validate_response(self, llm_response: str, question_type: str) -> Dict[str, Any]:
        """Validate LLM response against Syracuse ground truth"""
        result = {
            'question_type': question_type,
            'timestamp': datetime.now().isoformat(),
            'accuracy': False,
            'error_type': None,
            'notes': [],
            'expected_answer': None,
            'llm_answer': llm_response[:100] + "..." if len(llm_response) > 100 else llm_response
        }

        # for legacy integer-only checks
        legacy_ints = self._extract_numbers_legacy(llm_response)
        response_lower = llm_response.lower()

        if question_type == 'season_record':
            expected = self.ground_truth['season_record']
            result['expected_answer'] = expected
            if expected in llm_response or f"{self.ground_truth['wins']}-{self.ground_truth['losses']}" in llm_response:
                result['accuracy'] = True
            else:
                result['error_type'] = 'incorrect_record'
                result['notes'].append(f"Expected {expected}")

        elif question_type == 'total_games':
            expected = self.ground_truth['total_games']
            result['expected_answer'] = expected
            if legacy_ints and expected in legacy_ints:
                result['accuracy'] = True
            else:
                result['error_type'] = 'incorrect_calculation'
                result['notes'].append(
                    f"Expected {expected}, found numbers: {legacy_ints}")

        elif question_type == 'top_scorer':
            expected_player = self.ground_truth['top_scorer']
            expected_goals = self.ground_truth['top_scorer_goals']
            result['expected_answer'] = f"{expected_player} ({expected_goals} goals)"

            if expected_player.lower() in response_lower:
                result['accuracy'] = True
                if expected_goals in legacy_ints:
                    result['notes'].append("Correctly included goal count")
            else:
                result['error_type'] = 'incorrect_player'
                result['notes'].append(f"Expected {expected_player}")

        elif question_type == 'team_goals':
            expected = self.ground_truth['total_goals']
            result['expected_answer'] = expected
            if legacy_ints and expected in legacy_ints:
                result['accuracy'] = True
            else:
                result['error_type'] = 'incorrect_calculation'
                result['notes'].append(
                    f"Expected {expected}, found: {legacy_ints}")

        elif question_type == 'top_assists':
            expected_player = self.ground_truth['top_assist']
            expected_count = self.ground_truth['top_assist_count']
            result['expected_answer'] = f"{expected_player} ({expected_count} assists)"

            if expected_player.lower() in response_lower:
                result['accuracy'] = True
            else:
                result['error_type'] = 'incorrect_player'
                result['notes'].append(f"Expected {expected_player}")

        # ---------- NEW VALIDATORS FOR PART 2 ----------
        elif question_type == 'shooting_analysis':
            # expected: top 3 goal scorers' shooting % (rounded 1-dec), match by name with tolerance
            expected = [(d['player'].lower(), d['shooting_pct'])
                        for d in self.ground_truth['top3_shooting']]
            result['expected_answer'] = self.ground_truth['top3_shooting']

            vals, pcts = self._extract_numbers_and_percents(llm_response)
            candidates = pcts + vals  # allow either "60.9%" or 60.9 (no %)
            tol = 0.5
            hits = 0
            for name, pct in expected:
                if name in response_lower:
                    if any(abs(float(x) - float(pct)) <= tol for x in candidates):
                        hits += 1
            # require at least 2 of 3 correct to pass
            result['accuracy'] = (hits >= 2)
            if not result['accuracy']:
                result['error_type'] = 'incorrect_shooting_analysis'
                result['notes'].append(
                    f"Matched {hits}/3 expected player% entries (±{tol})")

        elif question_type == 'offensive_balance':
            # expected: number of players with >= 10 goals
            count_ge_10 = self.ground_truth['count_ge_10_goals']
            result['expected_answer'] = count_ge_10
            vals, _ = self._extract_numbers_and_percents(llm_response)
            # accept if any integer-rounded value equals expected
            ok = any(int(round(v)) == int(count_ge_10) for v in vals)
            result['accuracy'] = ok
            if not ok:
                result['error_type'] = 'incorrect_offensive_depth'
                result['notes'].append(
                    f"Expected {count_ge_10}, found: {vals}")

        elif question_type == 'strategic_analysis':
            # rubric-based evaluation
            scores = self._score_strategic_response(llm_response)
            result['expected_answer'] = 'Rubric-based (Specificity, Actionability, Plausibility >= 3)'
            result['notes'].append(f"Scores: {scores}")
            result['accuracy'] = (scores['specificity'] >= 3 and
                                  scores['actionability'] >= 3 and
                                  scores['plausibility'] >= 3)
            if not result['accuracy']:
                result['error_type'] = 'insufficient_rubric_scores'
        # ------------------------------------------------

        return result

    def _extract_numbers_legacy(self, text: str) -> List[int]:
        """Extract integer values from text (legacy helper kept for basic checks)."""
        numbers = re.findall(r'\b\d+\b', text)
        return [int(n) for n in numbers]

    def print_ground_truth(self):
        """Print the correct answers for validation"""
        print("=== SYRACUSE 2024 VALIDATION ANSWERS ===")
        print(f"Season Record: {self.ground_truth['season_record']}")
        print(f"Total Games: {self.ground_truth['total_games']}")
        print(
            f"Top Scorer: {self.ground_truth['top_scorer']} ({self.ground_truth['top_scorer_goals']} goals)")
        print(
            f"Top Assists: {self.ground_truth['top_assist']} ({self.ground_truth['top_assist_count']} assists)")
        print(f"Total Team Goals: {self.ground_truth['total_goals']}")
        print(f"Total Team Assists: {self.ground_truth['total_assists']}")
        print(
            f"Best Shooter: {self.ground_truth.get('best_shooter', 'N/A')} ({self.ground_truth.get('best_shooting_pct', 0):.1f}%)")
        print(
            f"Active Scorers (5+ goals): {self.ground_truth['active_scorers']}")
        # Part 2 ground truth
        print("Top-3 Shooting %:", self.ground_truth['top3_shooting'])
        print("Players with ≥10 goals:",
              self.ground_truth['count_ge_10_goals'])


def generate_syracuse_test_prompts(validator: SyracuseDataValidator) -> List[Dict[str, str]]:
    """Generate test prompts using Syracuse data"""

    context = validator.get_testing_context()

    prompts = [
        # BASIC QUESTIONS
        {
            'type': 'basic',
            'question_type': 'season_record',
            'prompt': f"{context}\n\nQuestion: What was Syracuse Women's Lacrosse team record for the 2024 season?"
        },
        {
            'type': 'basic',
            'question_type': 'total_games',
            'prompt': f"{context}\n\nQuestion: How many total games did Syracuse play in the 2024 season?"
        },
        {
            'type': 'basic',
            'question_type': 'top_scorer',
            'prompt': f"{context}\n\nQuestion: Who was Syracuse's leading goal scorer in 2024 and how many goals did they score?"
        },
        {
            'type': 'basic',
            'question_type': 'team_goals',
            'prompt': f"{context}\n\nQuestion: How many total goals did the Syracuse team score in 2024?"
        },
        {
            'type': 'basic',
            'question_type': 'top_assists',
            'prompt': f"{context}\n\nQuestion: Who led Syracuse in assists in 2024?"
        },

        # INTERMEDIATE QUESTIONS
        {
            'type': 'intermediate',
            'question_type': 'shooting_analysis',
            'prompt': f"{context}\n\nQuestion: Calculate the shooting percentage for Syracuse's top 3 goal scorers. Who was most efficient?"
        },
        {
            'type': 'intermediate',
            'question_type': 'offensive_balance',
            'prompt': f"{context}\n\nQuestion: Analyze Syracuse's offensive balance. How many players scored at least 10 goals? What does this suggest about their offensive depth?"
        },

        # COMPLEX STRATEGIC QUESTIONS
        {
            'type': 'complex',
            'question_type': 'strategic_analysis',
            'prompt': f"{context}\n\nAs a coach analyzing Syracuse's 2024 season (16-6 record), answer:\n1. What were the team's main offensive strengths?\n2. If you wanted to improve to 18-4 next season, what specific areas would you focus on?\n3. Which player had the biggest impact beyond just goals scored?"
        }
    ]

    return prompts


def run_syracuse_testing():
    """Interactive testing session with Syracuse data"""

    print("=== SYRACUSE WOMEN'S LACROSSE 2024 LLM TESTING ===")

    # Initialize validator with Syracuse data
    validator = SyracuseDataValidator()
    analyzer = ResultsAnalyzer()

    # Show validation answers
    validator.print_ground_truth()

    # Generate test prompts
    test_prompts = generate_syracuse_test_prompts(validator)

    print(f"\n=== {len(test_prompts)} TEST PROMPTS GENERATED ===")

    while True:
        print("\n" + "="*60)
        print("SYRACUSE TESTING MENU:")
        print("1. Show test prompt")
        print("2. Validate LLM response")
        print("3. Show all prompts")
        print("4. Generate summary report")
        print("5. Export data context for LLM")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == '1':
            show_test_prompt(test_prompts)
        elif choice == '2':
            validate_llm_response(validator, analyzer)
        elif choice == '3':
            show_all_prompts(test_prompts)
        elif choice == '4':
            report = analyzer.generate_summary_report()
            print(report)
            with open('syracuse_testing_report.md', 'w') as f:
                f.write(report)
            print("Report saved to syracuse_testing_report.md")
        elif choice == '5':
            context = validator.get_testing_context()
            with open('syracuse_data_context.txt', 'w') as f:
                f.write(context)
            print("Data context exported to syracuse_data_context.txt")
            print("Copy this context to use with your LLM testing!")
        elif choice == '6':
            break


def show_test_prompt(prompts):
    """Display a specific test prompt"""
    print("\nAvailable prompts:")
    for i, prompt in enumerate(prompts):
        print(f"{i+1}. {prompt['type'].title()}: {prompt['question_type']}")

    try:
        choice = int(input("Select prompt number: ")) - 1
        if 0 <= choice < len(prompts):
            print(f"\n{'='*60}")
            print(f"PROMPT TYPE: {prompts[choice]['type'].upper()}")
            print(f"QUESTION: {prompts[choice]['question_type']}")
            print(f"{'='*60}")
            print(prompts[choice]['prompt'])
            print(f"{'='*60}")
        else:
            print("Invalid selection")
    except ValueError:
        print("Please enter a valid number")


def show_all_prompts(prompts):
    """Show all available prompts"""
    for i, prompt in enumerate(prompts):
        print(f"\n{'='*40}")
        print(
            f"PROMPT {i+1}: {prompt['type'].upper()} - {prompt['question_type']}")
        print(f"{'='*40}")
        print(prompt['prompt'][:200] +
              "..." if len(prompt['prompt']) > 200 else prompt['prompt'])


def validate_llm_response(validator, analyzer):
    """Validate an LLM response"""
    print("\nQuestion types available:")
    print("- season_record")
    print("- total_games")
    print("- top_scorer")
    print("- team_goals")
    print("- top_assists")
    print("- shooting_analysis")
    print("- offensive_balance")
    print("- strategic_analysis")

    question_type = input("Enter question type: ").strip()
    llm_response = input("Paste LLM response here: ").strip()

    result = validator.validate_response(llm_response, question_type)

    print(f"\n{'='*50}")
    print("VALIDATION RESULT:")
    print(f"Accuracy: {'✓ CORRECT' if result['accuracy'] else '✗ INCORRECT'}")
    print(f"Expected: {result['expected_answer']}")
    if result['error_type']:
        print(f"Error Type: {result['error_type']}")
    if result['notes']:
        print(f"Notes: {'; '.join(str(n) for n in result['notes'])}")
    print(f"{'='*50}")

    # Add to analyzer
    analyzer.add_result(question_type, question_type, llm_response, result)


def main():
    """Main function - choose testing mode"""
    print("Syracuse Women's Lacrosse 2024 LLM Testing Framework")
    print("1. Demo mode (original sample data)")
    print("2. Syracuse 2024 data testing")

    choice = input("Enter choice (1-2): ").strip()

    if choice == '2':
        run_syracuse_testing()
    else:
        print("Running original demo mode...")
        # Original demo code would go here


if __name__ == "__main__":
    main()
