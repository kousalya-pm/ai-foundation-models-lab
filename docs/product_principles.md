# AI Product Principles Learned from the Lab

Ten principles this lab's experiments surfaced directly — each tied to the specific notebook that produced it, not asserted in the abstract.

1. **Diagnose the failure layer before choosing the intervention.** Notebook 08's failure taxonomy splits "wrong retrieval," "correct retrieval + wrong reasoning," and "correct retrieval + hallucination" into separate categories because each needs a different fix — better chunking, a different model, or a stricter grounding check, respectively. Treating "RAG gave a bad answer" as one problem leads to fixing the wrong layer. In the recorded run, the failure that actually occurred was neither retrieval nor reasoning but abstention: the model answered all 3 unanswerable questions instead of declining.

2. **Establish a baseline before optimization.** Every experiment in this lab is structured as baseline-then-intervention: notebook 05/08 measure the unaided model before adding retrieval; notebook 06 measures the base model before fine-tuning. Without the baseline, "6/9 correct with RAG" is a number with no reference point instead of a measured improvement over 0/9 unaided (strict keyword scoring).

3. **Fine-tuning is not automatically the answer.** Notebook 06's side-by-side comparison: LoRA took a general-purpose model from 33% to 67% accuracy, and did nothing for a security-specialized model already at 100%/83% — same technique, same dataset size, opposite outcome, because the second model had no gap left to close.

4. **RAG and fine-tuning solve different problems.** Notebook 08, Section 15: fine-tuning changes weights and behavior patterns; RAG changes context at inference time without touching weights, and only RAG can incorporate a policy that changed yesterday. Reaching for the wrong one costs a retraining cycle to fix a knowledge problem, or a document update to fix a behavior problem.

5. **Model metrics must connect to workflow/customer outcomes.** Notebook 07, Section 17 maps model-level metrics (MITRE precision/recall, groundedness, latency) to workflow metrics (investigation correctness, analyst trust, completion time) to business metrics (analyst productivity, adoption, MTTR) — a model metric that doesn't trace to one of these is a number nobody downstream should act on.

6. **Authority is different from model confidence.** Notebook 08, Section 14: a model can be 99% confident an account is compromised while the actual policy says a domain controller may never be automatically isolated regardless of confidence. Confidence is a property of the model's output; authority is a property of who — or what policy — is allowed to make the call.

7. **Deterministic business/security rules should not be casually overridden by an LLM.** The direct consequence of principle 6, made concrete in notebook 08's Acme policy set: two-person approval for privileged-account disablement, mandatory human approval before isolating a production endpoint — rules an LLM can recommend against but must never have the authority to execute around.

8. **Model changes require regression evaluation.** Notebook 07, Section 15 turns its own golden dataset into exactly this: a fixed suite run every time the model, prompt, or an upstream component (retrieval, fine-tuning) changes, scored on all eleven scorecard metrics together, not the one metric that happens to look best.

9. **AI observability must include prompts, retrieval, models, tools, latency, and cost.** Notebook 08, Section 17's request trace is the concrete list: query, retrieval, retrieved document IDs, retrieval scores, prompt/context, model version, response, latency, evaluation result. Missing any one of these turns "why did it give the wrong answer" into a guess instead of a diagnosis — this notebook could only separate retrieval failures from generation failures (Sections 7, 11, 12) because every one of these fields was captured.

10. **Model selection is a quality × latency × cost × risk decision, not a leaderboard lookup.** Notebook 07's scorecard puts 80% classification accuracy next to a 12.53s median latency in the same table on purpose — a model that scores marginally better but takes noticeably longer may be the wrong choice for an interactive workflow where an analyst is waiting mid-investigation. Quality alone never answers "which model should we ship."
