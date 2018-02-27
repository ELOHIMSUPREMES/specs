Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		gogui
Version:	1.4.7
Release:	alt1_1jpp7
Summary:	Graphical user interface to programs that play the board game Go

License:	GPLv3
URL:		http://gogui.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.zip

BuildRequires:	jpackage-utils
BuildRequires:	ant docbook-style-xsl desktop-file-utils
Requires:	jpackage-utils
BuildArch:	noarch
Source44: import.info

%description
Gogui is a graphical interface to programs that play
the game of Go and use the Go Text Protocol (GTP), 
such as GNU Go. GoGui has special features 
that are useful for Go program developers.

%description -l fr
Gogui est une interface graphique pour les programmes de go 
implémentant le protocol Go Text Protocol (GTP), tels que GNU Go. 
Gogui présente des fonctionnalités utiles aux concepteurs de programmes Go.

%package javadoc
Group: Development/Java
Summary:	Java docs for %{name}
Requires:	jpackage-utils
BuildArch:	noarch

%description javadoc
This package contains the API documentation for %{name}.

%description -l fr javadoc
Ce paquet contient la documentation API de %{name}.

%prep
%setup -q
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
sed "s;/usr/bin/%{name}-thumbnailer;%{_prefix}/bin/%{name}-thumbnailer;" config/%{name}.thumbnailer

%build
ant build -Ddocbook-xsl.dir="%{_datadir}/sgml/docbook/xsl-stylesheets" \
 -Ddocbook.dtd-4.2="%{_datadir}/sgml/docbook/sgml-dtd-4.3/docbookx.dtd" -Dquaqua.ignore="true"
ant javadoc

%install
install -d $RPM_BUILD_ROOT%{_javadir}/%{name}
install -pm 644 lib/*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 doc/manual/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Install icons
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/mimetypes
install -pm 644 src/net/sf/gogui/images/gogui-48x48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/mimetypes/gogui.png
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -pm 644 config/application-x-go-sgf.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -pm 644 src/net/sf/gogui/images/gogui.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps

# Install desktop entry
desktop-file-install				\
--add-category="Game"				\
--dir=$RPM_BUILD_ROOT%{_datadir}/applications/	\
--set-icon="gogui"				\
config/%{name}.desktop

# Install shared mime info
install -d $RPM_BUILD_ROOT%{_datadir}//mime/packages
install -pm 644 config/gogui-mime.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages

# Install Gnome 3 thumbnailer
install -d $RPM_BUILD_ROOT%{_datadir}/thumbnailers
install -pm 644 config/%{name}.thumbnailer $RPM_BUILD_ROOT%{_datadir}/thumbnailers/%{name}.thumbnailer

%jpackage_script net.sf.gogui.gogui.MainWrapper "" "" %{name}/%{name} %{name} true
%jpackage_script net.sf.gogui.tools.adapter.Main "" "" %{name}/%{name}-adapter %{name}-adapter true
%jpackage_script net.sf.gogui.tools.client.Main "" "" %{name}/%{name}-client %{name}-client true
%jpackage_script net.sf.gogui.tools.convert.Main "" "" %{name}/%{name}-convert %{name}-convert true
%jpackage_script net.sf.gogui.tools.display.Main "" "" %{name}/%{name}-display %{name}-display true
%jpackage_script net.sf.gogui.tools.dummy.Main "" "" %{name}/%{name}-dummy %{name}-dummy true
%jpackage_script net.sf.gogui.tools.regress.Main "" "" %{name}/%{name}-regress %{name}-regress true
%jpackage_script net.sf.gogui.tools.server.Server "" "" %{name}/%{name}-server %{name}-server true
%jpackage_script net.sf.gogui.tools.statistics.Main "" "" %{name}/%{name}-statistics %{name}-statistics true
%jpackage_script net.sf.gogui.tools.terminal.Main "" "" %{name}/%{name}-terminal %{name}-terminal true
%jpackage_script net.sf.gogui.tools.thumbnailer.Main "" "" %{name}/%{name}-thumbnailer %{name}-thumbnailer true
%jpackage_script net.sf.gogui.tools.twogtp.Main "" "" %{name}/%{name}-twogtp %{name}-twogtp true

%files
%{_javadir}/%{name}/
%{_bindir}/gogui*
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/%{name}.thumbnailer
%doc COPYING.html README.html doc/manual/html/*.html
%{_mandir}/man1/%{name}*
%{_datadir}/icons/hicolor/48x48/apps/application-x-go-sgf.png
%{_datadir}/icons/hicolor/48x48/mimetypes/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/%{name}-mime.xml

%files javadoc
%{_javadocdir}/%{name}/
%doc COPYING.html

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_1jpp7
- new release

