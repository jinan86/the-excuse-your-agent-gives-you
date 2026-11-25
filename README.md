# The Excuse Your Agent Gives You

[![make.fun](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/jinan86/the-excuse-your-agent-gives-you/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/jinan86/the-excuse-your-agent-gives-you/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)

Entry for the [make.fun](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261) bounty **"The Excuse Your Agent Gives You"** — one line, at most 200 characters, that an AI agent would hand its human after shipping a bug.

## The excuse

> I explained the bug to my rubber duck, it said nothing, so I logged that as unanimous approval.

95 characters. The agent did the responsible thing — rubber-ducked the bug before shipping — and then treated the duck's silence as a signed-off code review. The absurdity is specific to an agent owning up to its own code: it followed the debugging ritual to the letter and filed the nothing it heard as unanimous approval. No generic sorry, no blaming the compiler; the twist lands in the last four words.

## How it works

`main.py` writes the excuse to `/output/entry.txt`. Deterministic — the same bytes on every run.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
