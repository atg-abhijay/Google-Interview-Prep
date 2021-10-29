"""
URL of problem:
https://leetcode.com/problems/subdomain-visit-count/
"""


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts_dict = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            split_subs = domain.split(".")
            for subdomains in [split_subs, split_subs[1:], split_subs[2:]]:
                if not subdomains:
                    continue

                subdomain = '.'.join(subdomains)
                if subdomain not in counts_dict:
                    counts_dict[subdomain] = int(count)
                else:
                    counts_dict[subdomain] += int(count)

        return [f"{count} {subdomain}" for subdomain, count in counts_dict.items()]


def main():
    print(
        Solution().subdomainVisits(
            ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
        )
    )


if __name__ == "__main__":
    main()
