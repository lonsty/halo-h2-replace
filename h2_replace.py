import click
import jaydebeapi


def h2_replace(url, h2jar, user, passwd, ori_str, new_str):
    conn = jaydebeapi.connect("org.h2.Driver", # driver class
                              f"jdbc:h2:{url}", # JDBC url
                              [user, passwd], # credentials
                              h2jar) # location of H2 jar
    print(f"Connected to {url}.")
    
    try:
        curs = conn.cursor()
        curs.execute(f"UPDATE LINKS SET LOGO = REPLACE(LOGO, '{ori_str}', '{new_str}')")
        curs.execute(f"UPDATE OPTIONS SET OPTION_VALUE = REPLACE(OPTION_VALUE, '{ori_str}', '{new_str}')")
        curs.execute(f"UPDATE POSTS SET ORIGINAL_CONTENT = REPLACE(ORIGINAL_CONTENT, '{ori_str}', '{new_str}'), "
                     f"FORMAT_CONTENT = REPLACE(FORMAT_CONTENT, '{ori_str}', '{new_str}'), "
                     f"THUMBNAIL = REPLACE(THUMBNAIL, '{ori_str}', '{new_str}')")
        curs.execute(f"UPDATE THEME_SETTINGS SET SETTING_VALUE = REPLACE(SETTING_VALUE, '{ori_str}', '{new_str}')")
        curs.execute(f"UPDATE USERS SET AVATAR = REPLACE(AVATAR, '{ori_str}', '{new_str}')")
        print(f"Replaced '{ori_str}' with '{new_str}'")
    #     for value in curs.fetchall():
    #             # the values are returned as wrapped java.lang.Long instances
    #             # invoke the toString() method to print them
    #             print(value)
    finally:
        if curs is not None:
            curs.close()
        if conn is not None:
            conn.close()
        print('Closed cursor and disconnected from H2.')


@click.command(help="Replace the <original hostname> with the <new hostname>.")
@click.option('-o', '--ori-str', 'ori_str', help="original host.")
@click.option('-n', '--new-str', 'new_str', help="new hostname.")
@click.option('--url', 'url', default="./halo", show_default=True, help="H2 JDBC url.")
@click.option('--h2jar', 'h2jar', default="./h2.jar", show_default=True, help="location of H2 jar.")
@click.option('-u', '--user', 'user', default="admin", show_default=True, help="H2 database username.")
@click.option('-p', '--passwd', 'passwd', default="123456", show_default=True, help="H2 database password.")
def update(ori_str, new_str, url, h2jar, user, passwd):
    if not (ori_str and new_str):
        click.echo('Must give <ori-str> and <new-str>!')
        exit(1)

    h2_replace(url, h2jar, user, passwd, ori_str, new_str)
    click.echo('Done.')


if __name__ == '__main__':
    update()
