# MIT License
#
# Copyright (c) 2020 Hearot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import click

try:
    import config
except (ImportError, ModuleNotFoundError):
    print(
        "You need to create a configuration file "
        "named config.py. See config.sample.py."
    )
    exit(1)


@click.command()
@click.option("--mongodb-host", default=None, help="MongoDB host")
@click.option("--mongodb-password", default=None, help="MongoDB password")
@click.option("--mongodb-username", default=None, help="MongoDB username")
@click.option("--redis-database", default=None, help="Redis database")
@click.option("--redis-host", default=None, help="Redis host")
@click.option("--redis-password", default=None, help="Redis password")
@click.option("--redis-port", default=None, help="Redis port")
@click.option("--token", default=None, help="Telegram bot API token")
def run(
    mongodb_host: str,
    mongodb_password: str,
    mongodb_username: str,
    redis_database: int,
    redis_host: str,
    redis_password: str,
    redis_port: int,
    token: str,
):
    if mongodb_host:
        config.MONGODB_HOST = mongodb_host

    if mongodb_password:
        config.MONGODB_PASSWORD = mongodb_password

    if mongodb_username:
        config.MONGODB_USERNAME = mongodb_username

    if redis_database:
        config.REDIS_DATABASE = redis_database

    if redis_host:
        config.REDIS_HOST = redis_host

    if redis_password:
        config.REDIS_PASSWORD = redis_password

    if redis_port:
        config.REDIS_PORT = redis_port

    if token:
        config.TELEGRAM_TOKEN = token

    from bot.bot import bot

    bot.run()


if __name__ == "__main__":
    run()
