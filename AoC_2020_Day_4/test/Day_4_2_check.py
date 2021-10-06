from Passport_check import Passport_check
import re

class Day_4_2_check(Passport_check):

    @staticmethod
    def check_passport(mandatory_fields, line):
        """
        Checks that each passport field conforms to the policy

        Parameters
        ----------
        mandatory_fields : list
            list over required fields in passport
        line : str
            string representing the passport

        Returns
        -------
        bool:
            Returns True if passport conforms to the policy
        """
        BYR = ' byr:'
        IYR = ' iyr:'
        EYR = ' eyr:'
        HGT = ' hgt:'
        HCL = ' hcl:'
        ECL = ' ecl:'
        PID = ' pid:'

        if line is None or \
            BYR not in line or \
            IYR not in line or \
            EYR not in line or \
            HGT not in line or \
            HCL not in line or \
            ECL not in line or \
            PID not in line:
            return False

        for f in mandatory_fields:
            field_regex = r".*%s(\S+)\s?.*" % f
            f_val = re.sub(field_regex, r"\1", line)

            if (f == BYR and (not 1920 <= int(f_val) <= 2002)) or \
                (f == IYR and (not 2010 <= int(f_val) <= 2020)) or \
                (f == EYR and (not 2020 <= int(f_val) <= 2030)) or \
                (f == HCL and (re.search(r"^#[0-9a-f]{6}$", f_val)) is None) or \
                (f == PID and (re.search(r"^\d{9}$", f_val) is None)) or \
                (f == HGT and ('cm' not in f_val and 'in' not in f_val)) or \
                (f == HGT and \
                    ('cm' in f_val) and (not 150 <= int(f_val.replace("cm", "")) <= 193) or \
                (f == HGT and \
                    ('in' in f_val) and (not 59 <= int(f_val.replace("in", "")) <= 76)) or \
                (f == ECL and \
                    (re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", f_val) is None))):
                return False
        return True
