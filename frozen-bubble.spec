%include	/usr/lib/rpm/macros.perl
Summary:	Frozen Bubble arcade game
Summary(pl):	Gra zrêczno¶ciowa Frozen Bubble
Name:		frozen-bubble
Version:	1.0.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://people.mandrakesoft.com/~gc/fb/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Icon:		%{name}.xpm
URL:		http://www.frozen-bubble.org/
BuildRequires:	perl-devel
BuildRequires:	perl-SDL >= 1.19
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	SDL_mixer-devel >= 1.2.2
BuildRequires:	smpeg-devel
%requires_eq	perl
Requires:	perl-SDL >= 1.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(fbmdkcommon)"

%description
Full-featured, colorful animated penguin eyecandy, 50 levels of 1p
game, hours and hours of 2p game, 3 professional quality 20-channels
musics, 15 stereo sound effects, 7 unique graphical transition
effects.

%description -l pl
Gra o wielu mo¿liwo¶ciach, z kolorowymi animacjami, 50-ma poziomami
dla jednego gracza, wieloma godzinami zabawy dla dwóch graczy, 3-ma
profesjonalnej jako¶ci 20-kana³owymi muzyczkami, 15-ma
stereofonicznymi efektami d¼wiêkowymi, 7-ma unikalnymi graficznymi
efektami przej¶æ.

%prep
%setup -q

%build
%{__make} \
	OPTIMIZE="%{rpmcflags} -Wall" \
	PREFIX="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_pixmapsdir},%{_applnkdir}/Games}

%{__make} install PREFIX=$RPM_BUILD_ROOT/usr

install icons/%{name}-icon-48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS CHANGES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{perl_sitearch}/auto/*
%{perl_sitearch}/*.pm
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
%{_mandir}/man6/*
