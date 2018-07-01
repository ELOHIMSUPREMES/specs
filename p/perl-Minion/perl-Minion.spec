%define _unpackaged_files_terminate_build 1
%define sname minion

Name: perl-Minion
Version: 9.03
Release: alt1
Summary: Job queue
License: Artistic-2.0
Group: Development/Perl
Url: http://search.cpan.org/dist/Minion/
Source: %sname-%version.tar
BuildArch: noarch

BuildRequires: perl-devel
BuildRequires: perl(Mojolicious.pm)
BuildRequires: perl(Mojo/Pg.pm)

Requires: perl(Mojolicious.pm)

%description
Minion is a high performance job queue for the Perl programming language,
with support for multiple named queues, priorities, delayed jobs, job
dependencies, job progress, job results, retries with backoff, rate
limiting, unique jobs, statistics, distributed workers, parallel
processing, autoscaling, remote control, at http://mojolicious.org admin
ui, resource leak protection and multiple backends (such as at
http://www.postgresql.org).
Job queues allow you to process time and/or computationally intensive tasks
in background processes, outside of the request/response lifecycle of web
applications. Among those tasks you'll commonly find image resizing, spam
filtering, HTTP downloads, building tarballs, warming caches and basically
everything else you can imagine that's not super fast.

%prep
%setup -q -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendorlib/Minion*
%perl_vendorlib/Mojolicious*
%doc LICENSE README.md Changes

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 9.03-alt1
- initial build for ALT
