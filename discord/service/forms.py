import re

re_banoff = r'\/banoff\s0\s\w+\s\d+\s.+'
re_jailoff = r'\/jailoff\s\w+\s\d+\s.+'
re_muteoff = r'\/muteoff\s\w+\s\d+\s.+'
re_warnoff = r'\/warnoff\s\w+\s.+'
re_banipoff = r'\/banipoff\s\d+\.\d+\.\d+\.\d+.+'
re_givedemotalonoff = r'\/givedemotalonoff\s\w+\s\d+'
re_giveantijailoff = r'\/giveantijailoff\s\w+\s\d+'
re_giveantimuteoff = r'\/giveantimuteoff\s\w+\s\d+'

re_unapunishoff = r'\/unapunishoff\s\w+\s.+'
re_unban = r'\/unban\s\w+\s.+'
re_unjailoff = r'\/unjailoff\s\w+\s.+'
re_unmuteoff = r'\/unmuteoff\s\w+\s.+'
re_unwarnoff = r'\/unwarnoff\s\w+\s.+'
re_unbanip = r'\/unbanip\s\d+\.\d+\.\d+\.\d+'

pattern_list = (re_banoff, re_jailoff, re_muteoff, re_warnoff, re_banipoff, re_giveantijailoff, re_giveantimuteoff, re_givedemotalonoff,
                re_unapunishoff, re_unban, re_unjailoff, re_unmuteoff, re_unwarnoff, re_unbanip, )

def check_forms(commands: list) -> tuple:
    """ Робить перевірку commands по регулярних виразах.
        Повертає accepted_commands - команди які пройшли перевірку та
        commands - ті, які залишились. """
    accepted_commands = []
    failed_commands = []
    for command in commands:
        for pattern in pattern_list:
            if re.match(pattern, command):
                accepted_commands.append(command)
                break
        else:
            failed_commands.append(command)
    
    return accepted_commands, failed_commands


def make_results(commands: list, initial_str: str) -> str:
    """ Форматизує вивід правильних та неправильних форм. 
        Получає command та initial_str - початкову строку. """
    if len(commands) == 0:
        initial_str += '\n---'
        return initial_str
    for command in commands:
        initial_str += f'\n{command}'
    return initial_str