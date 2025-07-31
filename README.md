# Task_05_Descriptive_Stats

## Can Large Language Models Actually Analyze Sports Statistics?
### A Study Using Syracuse Women's Lacrosse 2024 Season Data

---

## Project Background

As someone working with data analysis and curious about the capabilities of LLMs like Claude and ChatGPT, I wanted to find out: **Can these AI systems actually understand and analyze sports statistics meaningfully?** 

For this research, I chose to focus on Syracuse University Women's Lacrosse 2024 season data. Having access to comprehensive player statistics from their 16-6 season seemed like the perfect opportunity to put LLMs through their paces with real-world data analysis challenges.

## What I'm Testing

The core question driving this research is whether LLMs can move beyond simple data regurgitation to provide genuine analytical insights that would be useful to coaches, players, or fans.

### My Testing Approach
I've designed three levels of questions to progressively challenge the LLMs:

**Level 1: Basic Data Retrieval**
- "What was the team's record this season?"
- "Who scored the most goals?"
- Simple factual questions that should be easy wins

**Level 2: Analytical Calculations** 
- "Calculate shooting percentages for the top scorers"
- "Which players provide the most balanced offensive contributions?"
- Questions requiring mathematical reasoning and comparisons

**Level 3: Strategic Insights**
- "What should the coach focus on to win more games next season?"
- "Which statistical improvements would have the biggest impact?"
- Questions demanding sports knowledge and strategic thinking

## The Syracuse 2024 Dataset

**Team Performance:** 16-6 record (22 games total)
- Home: 9-2 | Away: 5-2 | Conference: 9-1

**Key Players:**
- **Meaghan Tyrrell**: 70 goals, 32 assists (team leader in scoring)
- **Emma Ward**: 44 goals, 37 assists (team leader in assists) 
- **Olivia Adamson**: 58 goals, 25 assists
- **11 players** scored 5+ goals (showing good offensive depth)

The dataset includes complete statistics for 34 players covering goals, assists, shots, shooting percentages, and games played.

## My Testing Framework

I built a Python validation system that automatically checks LLM responses against the known correct answers. This removes human bias from accuracy assessment and ensures consistent evaluation.

### Tools Used
- **Python** for data processing and validation
- **Pandas** for statistical calculations
- **Claude Sonnet 4** as primary LLM for testing
- **Syracuse Official Statistics** as ground truth data source

## Initial Results (Part 1 - July 31, 2025)

After conducting my first round of systematic testing, here's what I discovered:

### **Perfect Performance on Basic Questions**
**Success Rate: 100% (5/5 tests)**

The LLM nailed every basic statistical question:
- Correctly identified the 16-6 season record
- Accurately named Meaghan Tyrrell as top scorer (70 goals)
- Properly calculated team totals (319 goals, 167 assists)
- Precisely identified Emma Ward as assist leader (37 assists)

### **What This Means**
LLMs excel at straightforward data retrieval when the information is clearly presented. No surprises here, but it's good to confirm the foundation is solid.

### **Next Phase Testing (August 15 Target)**
- Intermediate calculation questions
- Multi-step analytical reasoning
- Strategic coaching recommendations
- Cross-validation with other LLMs

## Repository Structure

```
Task_05_Descriptive_Stats/
├── README.md                           # This overview
├── Testing_and_Validation.py           # Main testing framework
├── syracuse_lacrosse_2024_real.csv     # Dataset (season statistics)
├── reports/
│   ├── july_31_progress.md            # Part 1 findings
│   └── testing_methodology.md         # Detailed approach
├── results/
│   ├── basic_questions_results.json   # Raw test results
│   └── validation_summaries/          # Analysis reports
└── prompts/
    ├── basic_prompts.txt              # Simple questions
    ├── intermediate_prompts.txt       # Calculation questions  
    └── strategic_prompts.txt          # Complex analysis questions
```

## Key Insights So Far

### What's Working Well
1. **Clear Data Presentation**: LLMs handle well-formatted statistics effectively
2. **Direct Questions**: Straightforward queries get accurate responses
3. **Validation Framework**: Automated checking catches errors reliably

### What I'm Curious About
1. **Calculation Complexity**: Will accuracy drop with multi-step math?
2. **Domain Knowledge**: Can LLMs demonstrate actual lacrosse understanding?
3. **Strategic Thinking**: Will recommendations be generic or insightful?

### Unexpected Discoveries
- The LLM consistently included context in responses (not just bare numbers)
- Response formatting was naturally appropriate for the question type
- No hallucination of player names or statistics encountered

## Methodology Notes

### Why Syracuse Women's Lacrosse?
- **Complete Dataset**: Full season statistics available
- **Manageable Size**: 34 players, 22 games - fits well in LLM context
- **Success Story**: 16-6 record provides both strengths and areas for analysis
- **Personal Interest**: Following the team made the research more engaging

### Validation Approach
Rather than subjectively judging whether answers "seem right," I built objective validation:
- Extract numerical values from LLM responses
- Compare against calculated ground truth
- Flag discrepancies automatically
- Track patterns in errors and successes

## Looking Ahead

### August 15 Goals
- Complete intermediate and complex question testing
- Compare Claude performance with ChatGPT and Copilot
- Develop "coaching recommendation" prompt templates
- Generate visualizations if LLMs can create them

### Research Questions to Explore
- Do different LLMs have different strengths in sports analysis?
- Can prompt engineering significantly improve complex reasoning?
- What's the ceiling for LLM sports analytics capabilities?

## How to Use This Framework

If you want to replicate this study or test LLMs with your own sports data:

1. **Prepare Your Dataset**: Clean CSV with player statistics
2. **Run the Framework**: `python Testing_and_Validation.py`
3. **Export Data Context**: Use option 5 to generate LLM-ready prompts
4. **Test Your LLM**: Copy prompts to Claude/ChatGPT/etc.
5. **Validate Results**: Use option 2 to check accuracy
6. **Generate Reports**: Use option 4 for summary analysis

## Personal Reflections

This research has been more interesting than I expected. While the basic results aren't surprising (LLMs are good at data retrieval), the process has revealed nuances in how these systems handle structured information.

I'm particularly curious to see how they perform on the strategic questions. Can an LLM provide coaching insights that would actually be useful? Or will the responses be generic advice that could apply to any team?

The validation framework has been invaluable - it's easy to think an LLM response "sounds good" without actually checking if it's correct. Systematic validation reveals gaps that casual evaluation might miss.

## Next Steps

- Continue testing through August 15
- Document the full range of LLM capabilities and limitations
- Create actionable recommendations for using LLMs in sports analytics
- Submit comprehensive findings for final evaluation

---

*All data sources are publicly available team statistics.*

**Contact**: arodr173@syr.edu  
**Course**: Research Methods  
**Instructor**: Dr. J. R. Strome (jrstrome@syr.edu)  
**Timeline**: July 2025 - August 2025
