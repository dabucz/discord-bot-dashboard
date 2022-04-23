import pymysql.cursors
import json
from Utils.config import get_mysql_host, get_mysql_username, get_mysql_password, get_mysql_db, get_default_prefix

def get_prefix_for_bot(bot, message):
    mysql = pymysql.connect(host=f'{get_mysql_host()}',user=f'{get_mysql_username()}',password=f'{get_mysql_password()}',database=f'{get_mysql_db()}',cursorclass=pymysql.cursors.DictCursor)
    with mysql:
        with mysql.cursor() as cursor:
                cursor.execute(f"SELECT prefix FROM prefixes WHERE guild = '{str(message.guild.id)}'")
                data = cursor.fetchone()
                if data:
                    mysql.commit()
                    return data["prefix"]
                else:
                    cursor.execute(f"INSERT INTO prefixes (guild, prefix) VALUES ('{str(message.guild.id)}', '{get_default_prefix()}')")
                    cursor.execute(f"SELECT prefix FROM prefixes WHERE guild = '{str(message.guild.id)}'")
                    data = cursor.fetchone()
                    if data:
                        mysql.commit()
                        return data["prefix"]

def setup():
    mysql = pymysql.connect(host=f'{get_mysql_host()}',user=f'{get_mysql_username()}',password=f'{get_mysql_password()}',database=f'{get_mysql_db()}',cursorclass=pymysql.cursors.DictCursor)
    with mysql:
        with mysql.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS prefixes (guild VARCHAR(255), prefix TEXT)")
        mysql.commit()

def register_guild(guild_id: int):
    mysql = pymysql.connect(host=f'{get_mysql_host()}',user=f'{get_mysql_username()}',password=f'{get_mysql_password()}',database=f'{get_mysql_db()}',cursorclass=pymysql.cursors.DictCursor)
    with mysql:
        with mysql.cursor() as cursor:
            cursor.execute(f"INSERT INTO prefixes (guild, prefix) VALUES ('{str(guild_id)}', '{get_default_prefix()}')")
        mysql.commit()

def unregister_guild(guild_id: int):
    mysql = pymysql.connect(host=f'{get_mysql_host()}',user=f'{get_mysql_username()}',password=f'{get_mysql_password()}',database=f'{get_mysql_db()}',cursorclass=pymysql.cursors.DictCursor)
    with mysql:
        with mysql.cursor() as cursor:
            cursor.execute(f"SELECT prefix FROM prefixes WHERE guild = '{str(guild_id)}'")
            data = cursor.fetchone()
            if data:
                cursor.execute(f"DELETE FROM prefixes WHERE guild = '{str(guild_id)}'")
        mysql.commit()

def setprefix(guild_id: int, prefix: str):
    mysql = pymysql.connect(host=f'{get_mysql_host()}',user=f'{get_mysql_username()}',password=f'{get_mysql_password()}',database=f'{get_mysql_db()}',cursorclass=pymysql.cursors.DictCursor)
    with mysql:
        with mysql.cursor() as cursor:
            cursor.execute(f"SELECT prefix FROM prefixes WHERE guild = '{str(guild_id)}'")
            data = cursor.fetchone()
            if data:
                cursor.execute(f"UPDATE prefixes SET prefix = '{prefix}' WHERE guild = '{str(guild_id)}'")
            else:
                cursor.execute(f"INSERT INTO prefixes (guild, prefix) VALUES ('{str(guild_id)}', '{get_default_prefix()}')")
                cursor.execute(f"SELECT prefix FROM prefixes WHERE guild = '{str(guild_id)}'")
                data = cursor.fetchone()
                if data:
                    cursor.execute(f"UPDATE prefixes SET prefix = '{prefix}' WHERE guild = '{str(guild_id)}'")
        mysql.commit()