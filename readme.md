# Building GPT from Scratch

Build a GPT model trained on the tiny_shakespeare dataset.

## Progress

- [x] Data preprocessing and tokenization
- [x] Bigram language model baseline
- [x] Token aggregation (building "memory")
- [x] Matrix multiplication for token communication
- [x] Softmax for attention weights
- [ ] Self-attention mechanism (in progress)
- [ ] Multi-head attention
- [ ] Transformer blocks
- [ ] Full GPT architecture

## What I've Learned

**Bigram Model**: Simplest language model - predicts next character based only on current character using probability distributions.

**Token Aggregation**: Added "memory" by allowing tokens to aggregate information from previous tokens using weighted averages.

**Softmax**: Converts raw scores into probability distributions for attention weights.

## Running the Code
```bash
python train.py
```

## Resources

- [Andrej Karpathy's "Let's build GPT" video](https://www.youtube.com/watch?v=kCc8FmEb1nY)
- Dataset: tiny_shakespeare

## Tech Stack

- PyTorch
- Python
