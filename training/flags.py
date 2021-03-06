import getpass
import os
import subprocess

import tensorflow as tf

from .envs import get_env


def validate_flags(FLAGS):
  messages = []
  if not FLAGS.env:
    messages.append("Missing required flag --env")
  if not FLAGS.hparams:
    messages.append("Missing required flag --hparams")

  if len(messages) > 0:
    raise Exception("\n".join(messages))

  return FLAGS


def update_hparams(FLAGS, hparams):
  hparams.model = FLAGS.model or hparams.model
  hparams.data = FLAGS.data or hparams.data
  hparams.env = FLAGS.env
  hparams.use_tpu = hparams.env == "tpu"
  hparams.train_steps = FLAGS.train_steps or hparams.train_steps
  hparams.eval_steps = FLAGS.eval_steps or hparams.eval_steps

  env = get_env(FLAGS.env)
  hparams.data_dir = os.path.join(FLAGS.data_dir or env.data_dir, hparams.data)
  hparams.output_dir = FLAGS.output_dir or os.path.join(env.output_dir, getpass.getuser(),
                                    FLAGS.hparams)

  return hparams
