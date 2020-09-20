default_train_config = {'num_iterations': 100000,  # number of iterations
                        'batch_size': 1,  # Batch size
                        'learning_rate': 0.00002,  # Learning rate for Adam
                        'accumulate_gradients': 1,  # Accumulate gradients across N minibatches.
                        'memory_saving_gradients': False,  # Use gradient checkpointing to reduce vram usage.
                        'only_train_transformer_layers': False,  # Restrict training to the transformer blocks.
                        'optimizer': 'adam',  # Optimizer. <adam|sgd>.
                        'noise': 0.0,  # Add noise to input training data to regularize against typos.

                        'top_k': 40,  # K for top-k sampling.
                        'top_p': 0.0,  # P for top-p sampling. Overrides top_k if set > 0.

                        'sample_every': 100,  # Generate samples every N steps
                        'sample_length': 1023,  # Sample this many tokens
                        'sample_num': 1,  # Generate this many samples
                        'save_every': 1000,  # Write a checkpoint every N steps
                        }