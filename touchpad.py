import subprocess

from i3pystatus import IntervalModule


class Touchpad(IntervalModule):
    """
    Some utils for touchpad. For example it allows you toggle touchpad click
    and more.

    """
    settings = (
        ("format", "formatp string"),
        ("yesno", "Yes/No string"),
    )
    format = "Touch: {status}"
    yesno = "No,Yes"

    on_leftclick = "toggle_tap_button"


    def get_tap_button_status(self):
        all_states = subprocess.check_output(["synclient"]).decode("utf-8").split("\n")
        off_state = next((s for s in all_states if 'tapbutton1' in s.lower()), None)
        return '= 1' in off_state

    def run(self):
        self.set_off()
        status = self.get_tap_button_status()
        cdict = {
            "status": self.yesno.split(",")[status]
        }
        self.output = {
            "full_text": self.format.format(**cdict)
        }

    def toggle_tap_button(self):
        value = "0" if self.get_tap_button_status() else "1"
        subprocess.check_call(['synclient', 'tapbutton1={}'.format(value)])

    def set_off(self):
        subprocess.check_call(['synclient', 'tapbutton1=0'])

