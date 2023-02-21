
## Step to run bible GPT:
```
$ python sample.py --out_dir=out-bible-char --num_samples=2 --max_new_tokens=200 --temperature=0.25 --device=cpu --start="God created the universe"
```

## Step to train
```
python train.py config/train_bible_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=1000 --lr_decay_iters=1000 --dropout=0.0 --dataset=bible_char
```

This will train the character as token model from scratch. This will run on any laptop or computer that does not have GPU.
More documentation can be found in the upstream repo karpathy/nanoGPT.
