%define upstream_name    CPAN-SQLite
%define upstream_version 0.200

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Maintain and search a minimal CPAN database
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Archive::Tar)
BuildRequires: perl(CPAN::DistnameInfo)
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Zlib)
BuildRequires: perl(LWP::Simple)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This package is used for setting up, maintaining, and searching a CPAN
database consisting of the information stored in the three main CPAN
indices: _$CPAN/modules/03modlist.data.gz_,
_$CPAN/modules/02packages.details.txt.gz_, and
_$CPAN/authors/01mailrc.txt.gz_. It should be considered at an alpha stage
of development.

One begins by creating the object as

  my $obj = CPAN::SQLite->new(%args);

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man?/*
%perl_vendorlib/*
%{_bindir}/cpandb
