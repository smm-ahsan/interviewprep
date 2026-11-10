#!/usr/bin/env python3
"""InterviewPrep - interview practice questions plus a STAR answer scaffold.

Pick a role, get a set of practice questions, and use the STAR scaffold
(Situation, Task, Action, Result) to structure strong answers.

Standard library only.
"""

import argparse
import random
import sys

STAR_LINE = (
    "  STAR scaffold: Situation - set the scene. Task - your responsibility. "
    "Action - what you did. Result - the outcome, with a number if you can."
)

DEFAULT_QUESTIONS = [
    "Tell me about yourself and why you want this job.",
    "What is your biggest strength, and how have you used it at work?",
    "Tell me about a time you faced a difficult problem at work. How did you handle it?",
    "Describe a time you worked under pressure to meet a deadline.",
    "Tell me about a mistake you made at work and what you learned from it.",
    "How do you prioritise when you have several tasks at the same time?",
    "Tell me about a time you worked well as part of a team.",
    "Why should we hire you over other candidates?",
    "Where do you see yourself in three years?",
    "Tell me about a time you received criticism. How did you respond?",
    "Describe a situation where you had to learn something new quickly.",
    "What questions do you have for us about this role?",
]

ROLE_BANKS = [
    (
        ("admin", "office"),
        [
            "How do you organise a busy schedule with competing appointments and deadlines?",
            "Which office software have you used for documents, spreadsheets and email, and how confident are you with each?",
            "How do you keep records accurate and easy for others to find later?",
            "Tell me about a time you had to rearrange a schedule at short notice. What did you do?",
            "How do you handle confidential information in an office environment?",
            "Describe how you would plan your first week organising files and records for a new manager.",
            "How do you deal with a colleague who keeps missing deadlines you depend on?",
        ],
    ),
    (
        ("market",),
        [
            "How would you promote a small local business with a very small budget?",
            "Which social media platforms do you know best, and what content works on each?",
            "Tell me about a post or campaign you created. How did you measure whether it worked?",
            "How do you decide what content to post when you have no new photos or videos?",
            "A client's post gets a negative comment in public. What do you do?",
            "How do you turn followers into actual customers or enquiries?",
        ],
    ),
    (
        ("cook", "chef", "kitchen"),
        [
            "How do you keep a kitchen station clean and organised during a busy service?",
            "Tell me about a time an order went wrong in the kitchen. How did you fix it?",
            "How do you check food quality and freshness before service starts?",
            "Which food safety and hygiene rules do you follow every single shift?",
            "How do you handle a sudden rush of orders when the kitchen is short-staffed?",
            "Describe a dish you are proud of and how you make sure it tastes the same every time.",
        ],
    ),
    (
        ("sales",),
        [
            "How do you approach a customer who is just looking and not ready to buy?",
            "Tell me about a difficult sale you turned around. What did you say?",
            "How do you handle a customer who says your price is too high?",
            "What do you do in the first minute with a new customer to build trust?",
            "How do you keep track of follow-ups so no customer is forgotten?",
            "Tell me about a time you beat a sales target. What made the difference?",
        ],
    ),
    (
        ("develop", "software", "program"),
        [
            "Tell me about a project you built. What was your role and what did you learn?",
            "How do you debug a problem when you have no idea where the bug is?",
            "How do you decide between fixing code quickly and rewriting it properly?",
            "Tell me about a time you had to learn a new tool or language for a task.",
            "How do you explain a technical problem to someone non-technical?",
            "What do you check before you call a piece of work finished?",
        ],
    ),
    (
        ("customer", "support"),
        [
            "How do you calm down an angry customer who is raising their voice?",
            "Tell me about a time you turned an unhappy customer into a happy one.",
            "A customer asks for something company policy does not allow. What do you say?",
            "How do you handle several customers waiting at the same time?",
            "What does good customer service mean to you, in one real example?",
            "How do you stay patient when a customer repeats the same complaint?",
        ],
    ),
]


def pick_questions(role, count, rng):
    role_lower = role.lower()
    role_bank = []
    for keywords, bank in ROLE_BANKS:
        if any(keyword in role_lower for keyword in keywords):
            role_bank = list(bank)
            break

    rng.shuffle(role_bank)
    default_bank = [q for q in DEFAULT_QUESTIONS if q not in role_bank]
    rng.shuffle(default_bank)

    pool = role_bank + default_bank
    return pool[: max(0, min(count, len(pool)))]


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="InterviewPrep: interview practice questions with a STAR answer scaffold."
    )
    parser.add_argument("--role", required=True, help="The job role you are preparing for, free text.")
    parser.add_argument("--count", type=int, default=6, help="How many questions to print (default 6).")
    parser.add_argument("--seed", type=int, default=1, help="Random seed for repeatable sets (default 1).")
    args = parser.parse_args(argv)

    rng = random.Random(args.seed)
    questions = pick_questions(args.role, args.count, rng)

    print(f"Interview practice for: {args.role}")
    print()
    for i, question in enumerate(questions, start=1):
        print(f"{i}. {question}")
        if i <= 2:
            print(STAR_LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
