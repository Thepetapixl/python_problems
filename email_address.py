# Every
# email
# consists
# of
# a
# local
# name and a
# domain
# name, separated
# by
# the @ sign.
#
# For
# example, in alice @ leetcode.com, alice is the
# local
# name, and leetcode.com is the
# domain
# name.
#
# Besides
# lowercase
# letters, these
# emails
# may
# contain
# '.'
# s or '+'
# s.
#
# If
# you
# add
# periods('.')
# between
# some
# characters in the
# local
# name
# part
# of
# an
# email
# address, mail
# sent
# there
# will
# be
# forwarded
# to
# the
# same
# address
# without
# dots in the
# local
# name.For
# example, "alice.z@leetcode.com" and "alicez@leetcode.com"
# forward
# to
# the
# same
# email
# address.(Note
# that
# this
# rule
# does
# not apply
# for domain names.)
#
# If
# you
# add
# a
# plus('+') in the
# local
# name, everything
# after
# the
# first
# plus
# sign
# will
# be
# ignored.This
# allows
# certain
# emails
# to
# be
# filtered,
# for example m.y + name @ email.com will be forwarded to my @ email.com.(this rule does not apply for domain names.)
#
# It is possible
# to
# use
# both
# of
# these
# rules
# at
# the
# same
# time.
#
# Given
# a
# list
# of
# emails, we
# send
# one
# email
# to
# each
# address in the
# list.How
# many
# different
# addresses
# actually
# receive
# mails?
#
#
#
# Example
# 1:
#
# Input: ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com"
# actually
# receive
# mails
#
# Note:
#
# 1 <= emails[i].length <= 100
# 1 <= emails.length <= 100
# Each
# emails[i]
# contains
# exactly
# one
# '@'
# character.
# All
# local and domain
# names
# are
# non - empty.
# Local
# names
# do
# not start
# with a '+' character.


def email(mails):
    actual_mail = ""
    found_mail = {}
    check = False
    i = 0
    for mail in mails:
        while i < len(mail):
            if mail[i] == '.' and check is False:
                i += 1
                continue

            elif mail[i] == '+':
                while mail[i] != '@':
                    i += 1
                check = True
            if mail[i] == '@':
                check = True
            actual_mail += mail[i]
            i += 1
        found_mail[actual_mail] = True
        actual_mail = ""
        i = 0
        check = False
    print(len(found_mail))


mail_list = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
email(mail_list)
