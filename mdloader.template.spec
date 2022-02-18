%define debug_package %{nil}

Name:       {{{ git_dir_name }}}
Version:    {{{ git_dir_version }}}
Release:    1%{?dist}
Summary:    This is a test package.

BuildRequires:  make gcc

License:    GPLv3
URL:        https://github.com/Massdrop/mdloader
VCS:        {{{ git_dir_vcs }}}

Source:     {{{ git_dir_pack }}}

%description
This is a test package.

%prep
{{{ git_dir_setup_macro }}}

%build
make

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 build/mdloader %{buildroot}/%{_bindir}

%files
%license LICENSE
%{_bindir}/mdloader

%changelog
{{{ git_dir_changelog }}}