import re

class Passport_check:

    @staticmethod
    def valid(mandatory_fields, line):
        for mandatory_field in mandatory_fields:
            if mandatory_field not in line:
                return False
        return True

    @staticmethod
    def is_valid_fields(mandatory_fields, line):
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