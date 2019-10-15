#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Mail
%define		pnam	Transport
%include	/usr/lib/rpm/macros.perl
Summary:	Mail::Transport - use Mail Transfer Agents (MTAs)
Name:		perl-Mail-Transport
Version:	3.004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6294dc02c2a75e0b0f21fa16a4493f28
URL:		https://metacpan.org/release/Mail-Transport/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Mail-Message >= 3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Objects which extend Mail::Transport implement sending and/or
receiving of messages, using various protocols.

Mail::Transport::Send extends this class, and offers general
functionality for send protocols, like SMTP.  Mail::Transport::Receive
also extends this class, and offers receive method.  Some transport
protocols will implement both sending and receiving.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Mail/*.pm
%{perl_vendorlib}/Mail/Transport
%{_mandir}/man3/*
