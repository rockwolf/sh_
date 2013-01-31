#!/usr/bin/perl

# gimap.pl by gxmsgx
# description: get the count of unread messages on gmail imap
#
# instructions:
#
# * * * * * ~/scripts/mailcount.pl > /var/log/mailcount
# and read mailcount in tail/turbotail (systail)

use strict;
use Mail::IMAPClient;
use IO::Socket::SSL;

my $username = 'example.username'; # example.username@gmail.com
my $password = 'password123';

my $socket = IO::Socket::SSL->new(
  PeerAddr => 'imap.gmail.com',
  PeerPort => 993,
  )
  or die "socket(): $@";

my $client = Mail::IMAPClient->new(
  Socket  => $socket,
  User    => $username,
  Password => $password,
  )
  or die "new(): $@";

if ($client->IsAuthenticated()) {
    my $msgct;

    $client->select("INBOX");
    $msgct = $client->unseen_count||'0';
    print "$msgct\n";
}
