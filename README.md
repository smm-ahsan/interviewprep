# InterviewPrep

A tiny open-source CLI that gives you interview practice questions for your target role, plus a STAR answer scaffold to structure strong answers.

## What STAR means

STAR is a simple way to answer "tell me about a time when..." questions:

- **Situation** — set the scene.
- **Task** — your responsibility.
- **Action** — what you did.
- **Result** — the outcome, with a number if you can.

InterviewPrep prints the STAR scaffold after the first two questions of every set, so you build the habit while you practise.

## Role banks covered

- Office and administration (roles containing "admin" or "office")
- Marketing (roles containing "market")
- Kitchen (roles containing "cook", "chef" or "kitchen")
- Sales (roles containing "sales")
- Developer (roles containing "develop", "software" or "program")
- Customer service (roles containing "customer" or "support")

If your role matches a bank, you get that bank's questions first, topped up with general questions. Any other role gets the general question bank.

## Requirements

- Python 3
- Standard library only, nothing to install

## Usage

```bash
python3 interviewprep.py --role "office administrator" --count 4 --seed 2
python3 interviewprep.py --role "astronaut" --count 3 --seed 2
```

Options:

- `--role` (required) — the job role you are preparing for, free text.
- `--count` — how many questions to print (default 6).
- `--seed` — random seed, so the same seed gives the same set (default 1).

See `examples.md` for real output.

## License

MIT — see `LICENSE`.
