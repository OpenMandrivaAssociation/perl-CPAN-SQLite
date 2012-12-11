%define upstream_name    CPAN-SQLite
%define upstream_version 0.202

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Maintain and search a minimal CPAN database
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(CPAN::DistnameInfo)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Zlib)
BuildRequires:	perl(LWP::Simple)
BuildArch:	noarch

%description
This package is used for setting up, maintaining, and searching a CPAN
database consisting of the information stored in the three main CPAN
indices: _$CPAN/modules/03modlist.data.gz_,
_$CPAN/modules/02packages.details.txt.gz_, and
_$CPAN/authors/01mailrc.txt.gz_. It should be considered at an alpha stage
of development.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man?/*
%{perl_vendorlib}/*
%{_bindir}/cpandb

%changelog
* Sun Jun 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.202.0-1mdv2011.0
+ Revision: 687339
- update to new version 0.202

* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.201.0-1
+ Revision: 686620
- update to new version 0.201

* Wed Jun 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.200.0-1
+ Revision: 685307
- update to new version 0.200

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.199.0-2
+ Revision: 653427
- update file list
- rebuild for updated spec-helper

* Wed Dec 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.199.0-1mdv2011.0
+ Revision: 483883
- update to 0.199

* Mon Sep 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.198.0-1mdv2010.0
+ Revision: 446429
- update to 0.198

* Wed Aug 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.197.0-1mdv2010.0
+ Revision: 415307
- import perl-CPAN-SQLite


* Wed Aug 12 2009 cpan2dist 0.197-1mdv
- initial mdv release, generated with cpan2dist
