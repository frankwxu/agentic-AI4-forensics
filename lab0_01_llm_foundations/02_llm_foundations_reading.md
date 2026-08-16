# Lab 0-01 Reading: What Is an LLM?

This reading gives you a teaching-friendly picture of what a large language model is and what it is not. The goal is not to cover every detail of modern AI systems. The goal is to help you build a usable mental model before you start the setup, prompt, and agent labs.

This lab also includes a runnable notebook, [03_tiny_llm_book_demo.ipynb](03_tiny_llm_book_demo.ipynb), where you will train a tiny word-level transformer on a short public-domain book excerpt and inspect its next-word predictions.

![Figure 1. From text input to next-token output in an LLM](./figures/lab0_llm_pipeline.svg)

*Figure 1. A teaching-friendly LLM pipeline: text becomes tokens, tokens become token IDs, token IDs become initial token meanings (embeddings), the transformer turns those into contextualized token meanings, and the output layer scores many possible next tokens. The figure shows only the top few probabilities so they are easy to read.*

## 1. What Is an LLM?

An `LLM`, or large language model, is a type of AI model that excels at understanding and generating human language. It is trained on large amounts of text to recognize language patterns and can interpret the wording and context of an input well enough to produce a useful response. This capability does not prove human-like comprehension or guarantee that its response is factually correct or supported by evidence.

Under the hood, the central job is simpler: predict the next token from the text that came before it. When you ask a question, the model does not look up a hidden answer sheet in the way a database would. Instead, it uses patterns learned from training data to score possible next tokens, selects one, and repeats that step again and again.

In plain language, an LLM is:

- a model that reads text as tokens
- a model that uses prior context to predict what should come next
- a model that can generate useful language without guaranteeing human-like understanding, factual correctness, or evidence-based conclusions

This is why an LLM can produce responses that sound fluent, organized, and confident, even when parts of the answer are incomplete or wrong.

**Examples of LLMs.**

The following are representative LLM families and their providers:

| Model | Provider |
| --- | --- |
| Deepseek-R1 | DeepSeek |
| GPT4 | OpenAI |
| Llama 3 | Meta (Facebook AI Research) |
| SmolLM2 | Hugging Face |
| Gemma | Google |
| Mistral | Mistral |

For a second, approachable explanation, see Hugging Face's [What are LLMs?](https://huggingface.co/learn/agents-course/en/unit1/what-are-llms) lesson.

## 2. What a Transformer Does at a High Level

The `transformer` is the model architecture that made modern LLMs practical at scale. Most current LLMs are built on this deep-learning architecture, which uses an `attention` mechanism to decide which parts of the input matter most for the current prediction. Transformers were introduced in 2017, and their adoption grew rapidly after models such as Google's BERT in 2018.

If you would like to see the original encoder--decoder Transformer design, see the diagram in the paper [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762).

> **Important:** The diagram below shows the original encoder--decoder Transformer, which was designed for sequence-to-sequence tasks such as translation. Llama and GPT-style chat LLMs use only a decoder stack: the same layers process the prompt and generate the next token.

![Transformer attention architecture](https://machinelearningmastery.com/wp-content/uploads/2021/08/attention_research_1.png)

*Figure 2. The original encoder--decoder Transformer architecture, designed for sequence-to-sequence tasks such as translation.*

**Three Transformer Families.**

Transformers are commonly grouped by the job they perform:

- `encoder-based` Transformers take text (or other data) as input and turn it into a dense representation, also called an embedding. BERT is a well-known example. These models are useful for text classification, semantic search, and named-entity recognition.
- `decoder-only` Transformers generate a sequence one token at a time. Llama is one example. This is the usual architecture for chat-oriented LLMs, text generation, and code generation; such models often have billions of parameters.
- `encoder--decoder`, or sequence-to-sequence, Transformers first encode the input into a context representation and then decode an output sequence. T5 and BART are examples. They are often used for translation, summarization, and paraphrasing.

Although language models come in several forms, the LLMs used in chat systems are typically large decoder-only Transformers. Their repeated next-token generation is the principle this reading focuses on.

Because this course focuses on chat-style LLMs, the diagram below shows a decoder-only Transformer. Its masked self-attention layers process the prompt and previously generated tokens, then predict one next token at a time.

![Decoder-only LLM architecture](./figures/decoder_only.jpg)

*Figure 3. The GPT-1 architecture without the task-classifier head (left) and the GPT-2 architecture (right). Source: [Meet GPT: The Decoder-Only Transformer](https://towardsdatascience.com/meet-gpt-the-decoder-only-transformer-12f4a7918b36/).*

For this course, treat the `decoder-only Transformer` as a black box with a clear job:

- input: the tokens seen so far, represented as embeddings
- internal work: update those token meanings in relation to one another inside the allowed context window
- output: contextualized token meanings that can be used to score the next token

One helpful way to think about the internal pieces is:

- `tokenizer`: turns text into token IDs
- `embeddings`: give each token an initial meaning
- `transformer blocks`: update token meanings using surrounding context
- `output layer`: converts the current contextualized state into next-token scores
- `sampler`: selects the next token from those scores

The next two sections explain tokens and embeddings. After that, you will see how a transformer uses surrounding context to update those initial meanings before making a prediction.

## 3. How Text Becomes Tokens

Models do not read raw text the way humans do. They first break text into smaller pieces called `tokens`.

Depending on the tokenizer, a token might be:

- a whole short word
- part of a longer word
- punctuation
- whitespace patterns
- a symbol or number chunk

For example, the sentence:

```text
Dorothy ran home.
```

might be broken into pieces like:

```text
["Dorothy", " ran", " home", "."]
```

The exact split depends on the tokenizer. The important point is that models work with token sequences, not with human-friendly word boundaries.

Many tokenizers use subword pieces, which lets a limited vocabulary represent many different words. For example, `interest` and `ing` can combine to form `interesting`, while `ed` can be added to form `interested`.

### Tokenization Example

You can picture tokenization as a first pass that turns text into chunks the model can work with, and then assigns each chunk an ID.

For example:

```text
Original text:
Dorothy ran home.

Possible token sequence:
["Dorothy", " ran", " home", "."]

Possible token IDs:
[17, 42, 9, 3]
```

The model does not yet know what these chunks mean. At this stage, it has an ordered sequence of pieces and a numeric ID for each piece.

In the tiny notebook for this lab, we simplify even further and use `word-level tokens`, so each word is treated as one token. Real production LLMs often use more flexible tokenizers that can split longer words into smaller parts.

### Try It: Tokenizer Playground

Use the interactive Hugging Face tokenizer playground to see how different tokenizers split your own text into tokens:

<iframe src="https://agents-course-the-tokenizer-playground.static.hf.space" title="Hugging Face Tokenizer Playground" width="100%" height="520"></iframe>

If the interactive view is not available in your Markdown preview, open the [Tokenizer Playground](https://agents-course-the-tokenizer-playground.static.hf.space) in a new tab.

### Why This Matters

- A single word can become multiple tokens.
- A prompt with more tokens uses more of the model's context window.
- Small wording changes can change the token sequence and therefore change the output.

## 4. From Token IDs to Initial Token Meanings

Token IDs are only labels. Before the model can do useful math with them, it looks up each ID in an embedding table and turns it into a small vector of learned numbers.

That is the role of `embeddings`: they give each token an initial meaning the model can work with numerically.

### Embedding Lookup Example

Students often ask what an embedding actually is. A simple answer is: it is a row of learned numbers attached to a token.

For example, a tiny teaching model might store something like:

```text
"dorothy" -> token ID 17 -> [0.21, -0.44, 0.08, 0.91]
"ran"     -> token ID 42 -> [0.18, -0.39, 0.11, 0.87]
"home"    -> token ID 63 -> [-0.72, 0.55, 0.14, -0.31]
```

![Figure 4. Visualizing one embedding lookup](./figures/lab0_embedding_lookup.svg)

*Figure 4. A token does not carry meaning as raw text or as an ID alone. The model uses the token ID to look up one learned row of numbers in the embedding table, giving that token an initial meaning before context is applied.*

Those numbers are not meant for people to read directly. They are values the model learns so it can process tokens mathematically.

One helpful mental model is:

- tokenization gives the model token pieces
- token IDs give each token a lookup key
- embeddings give each token a learned numeric row from a table

So when students ask, "What does an embedding look like?", the shortest correct answer is:

`a small vector of learned numbers attached to a token`

You do not need to interpret each number by itself. What matters is that the model uses those numbers as the token's starting meaning before context is applied.

### From Initial to Contextualized Meanings

The transformer updates each token's starting embedding using the surrounding tokens. The resulting contextualized meaning can differ across sentences. For example, `bank` can point toward different meanings in a river sentence versus a money sentence. Attention lets the model give greater weight to the words that reveal which meaning is intended.

![Figure 5. Context words disambiguate bank](./figures/lab0_bank_attention_context.png)

*Figure 5. Context words distinguish the river meaning of `bank` from its financial-institution meaning. Attention helps the model identify the words most useful for making that distinction. Source: [Cohere, What Is Attention in Language Models?](https://cohere.com/llmu/what-is-attention-in-language-models).*

The two contexts then lead to different contextualized embeddings. In this teaching illustration, `bank1` is closer to river-related ideas and `bank2` is closer to money-related ideas; the percentages show an illustrative weighting, not a calculation students need to perform.

![Figure 6. Context changes the embedding of bank](./figures/lab0_bank_contextual_embeddings.png)

*Figure 6. A teaching visualization of contextualized embeddings. The same token, `bank`, is represented differently when its surrounding context points toward a river or toward money. Source: [Cohere, What Is Attention in Language Models?](https://cohere.com/llmu/what-is-attention-in-language-models).*

The attention mechanism represents these relationships as numeric scores between token positions. The example below gives `bank` a nonzero relationship with `river` in the first sentence and with `money` in the second.

![Figure 7. Attention-score matrices for bank](./figures/lab0_bank_attention_scores.png)

*Figure 7. A simplified attention-score matrix for the two `bank` contexts. The numbers are illustrative attention relationships, not probabilities students need to calculate. Source: [Cohere, What Is Attention in Language Models?](https://cohere.com/llmu/what-is-attention-in-language-models).*

The following simplified view makes the same contrast explicit: one starting embedding for `bank` is updated into different contextualized representations.

![Figure 8. The same token can change meaning across contexts](./figures/lab0_contextualized_bank.svg)

*Figure 8. The token `bank` can start with one initial embedding, but the transformer updates it differently in a river sentence versus a money sentence.*

### Context Windows

The `context window` is the amount of recent text the model is allowed to consider at one time when predicting the next token. For example, if a tiny model could only look at the last 6 tokens, then:

```text
... Aunt Em called, and Dorothy ran home
```

the model might only "see" something like:

```text
["Em", "called", ",", "Dorothy", "ran", "home"]
```

Anything earlier than that would fall outside the current window. More useful recent context often leads to better next-token predictions.

## 5. What the Model Predicts

At each generation step, the model takes the current contextualized token meanings and produces a probability distribution over possible next tokens.

To keep one running example, the next few sections continue with the same tiny sentence.

For example, after the text:

```text
Dorothy ran
```

the model might internally lean toward possibilities such as:

- ` home`
- ` away`
- ` back`

The model does not simply "know" one correct next token. It scores many possibilities and the system then selects or samples one.

The output layer scores the whole vocabulary, but Figure 1 shows only a small top-token slice so the probabilities are easy to read.

This is the core loop:

1. read the current token sequence
2. turn token IDs into embeddings
3. use the transformer to update those meanings with context
4. score possible next tokens
5. choose one token
6. append it to the sequence
7. repeat

That is what people mean by `next-token prediction`.

### Next-Token Prediction Example

Suppose the current text is:

```text
Dorothy ran
```

The model may score possible next tokens something like this:

```text
" home"      0.72
" away"      0.18
" back"      0.07
other tokens 0.03 combined
```

That does not mean the model has proven Dorothy ran home. It means that, given the words so far, `home` currently looks like the most likely next token.

## 6. Training Versus Using a Model

Students often blur `training` and `inference`, so keep them separate:

- `training`: the model's internal weights are updated so it gets better at prediction
- `inference`: the model uses its current weights to generate an output, but the weights do not change

`Weights` are the internal learned numbers of the model. During training, the model adjusts those numbers a little at a time so its predictions get better.

During training, the model repeatedly predicts tokens, compares its predictions with the training text, measures error, and updates its weights to reduce that error over time.

During inference, the model does not learn from your single prompt in the normal sense. It is only using what it already learned plus the context you provided in the current input.

This distinction matters later in the course:

- prompt engineering changes the input context during inference
- it does not retrain the model
- agent workflows add structure and tools around inference
- they do not magically remove model limitations

### A Tiny Analogy for Weights

If the word `weights` still feels abstract, it can help to look at a much simpler model first.

![Figure 9. A tiny regression analogy for weights](./figures/lab0_weights_regression.svg)

*Figure 9. This is not an LLM. It is a small line-fitting example used only to show what a weight is. Training changes the model's internal numbers so its predictions move closer to the data.*

### A Training Example

Here is a tiny teaching example:

```text
Input context:   "Dorothy ran"
Target next word: "home"
```

The model makes a prediction such as:

```text
"home"  0.72
"away"  0.18
"back"  0.07
```

If the correct next word is `home`, the model is mostly right but still imperfect. Training uses that error signal to adjust the model's weights a little bit.

After many examples, the model becomes better at predicting likely next tokens from similar contexts.

This is why training and inference feel different:

- training changes the model
- inference uses the current model

## 7. Why Prompting Changes Outputs

Prompts matter because prompts are part of the token context.

If you ask:

```text
Continue the sentence:
Dorothy ran
```

you give the model a broad context with few boundaries.

If you ask:

```text
Continue the sentence with exactly one word:
Dorothy ran
```

you change the token context and make some next-token paths more likely than others.

This is why prompt wording can influence:

- format
- level of detail
- caution or certainty
- consistency across runs

### Temperature

`Temperature` changes how deterministic or variable token selection becomes.

If the model scores three next tokens with similar probabilities, then:

- lower temperature makes the output more conservative and predictable
- higher temperature makes the output more varied and more surprising

In simple terms:

- low temperature: "pick safer high-probability tokens"
- high temperature: "allow lower-probability tokens more often"

That is one reason the same prompt can produce different outputs across runs or settings.

### Temperature Example

Suppose the next-token probabilities are:

```text
"home"  0.72
"away"  0.18
"back"  0.10
```

At lower temperature, the system is more likely to keep choosing `home`.

At higher temperature, `away` or `back` become more likely to appear, even though they started with lower scores.

## 8. Why LLM Limits Matter for Forensics and Agents

In digital forensics, fluent text is not enough. The answer also has to stay bounded by evidence.

An LLM-only workflow can run into problems such as:

- inventing details that were not in the evidence
- overstating certainty
- drifting away from the required output format
- missing key context when the prompt is too broad
- sounding persuasive even when the underlying reasoning is weak

These are not bugs in only one model. They are reasons the later labs add structure around the model.

![Figure 10. Why the course adds more than an LLM alone](./figures/lab0_llm_limits_to_controls.svg)

*Figure 10. LLM-only behavior is useful but not always reliable enough for bounded forensic tasks. The rest of the course adds prompt rules, tools, memory, planning, multiagent review, and human judgment around the model.*

This course responds to those limits in stages:

- `lab0_03_model_warmup`: show that prompt wording and model choice change outputs
- `lab0_04_what_is_an_agent`: show how the same model behaves differently inside a bounded workflow
- `lab1` through `lab5`: add reflection, tools, step-by-step reasoning, planning, and multiagent review

The big course idea is not that an LLM becomes perfect once you wrap it in a workflow. The idea is that well-designed structure makes the model's behavior easier to inspect, constrain, and review.

## 9. Short Reflection Questions

Use these questions to check your understanding:

1. In one or two sentences, what does an LLM predict at each generation step?
2. Why is a token not always the same thing as a word?
3. What is the difference between training a model and using a model at inference time?
4. Why can two prompts about the same topic produce different answers?
5. Why can an LLM sound confident and still be wrong?
6. Name one reason later labs add tools, memory, or human review around the model.

## Notebook Bridge

When you open [03_tiny_llm_book_demo.ipynb](03_tiny_llm_book_demo.ipynb), watch for these connections:

- the corpus text becomes a sequence of word-level tokens
- token IDs are turned into initial token meanings through embeddings
- the transformer updates those into contextualized token meanings
- training lowers loss by improving next-word predictions on that small corpus
- inference uses the trained model to score and sample likely next words
- the model can still sound fluent while remaining limited by its size, data, and context

## Key Takeaways

If you remember only three things from this primer, keep these:

- an LLM works by predicting the next token from context
- prompt wording changes that context and therefore changes output behavior
- later labs add structure because language fluency alone is not enough for careful forensic work

When you are ready, move on to [lab0_02_environment_setup/01_instructions.md](../lab0_02_environment_setup/01_instructions.md).
