from qutebrowser.config.configfiles import ConfigAPI  # make lsp shut up
from qutebrowser.config.config import ConfigContainer
import subprocess
config: ConfigAPI = config
c: ConfigContainer = c

config.load_autoconfig(False)

def adblkinstall():
  subprocess.run(["pip", "install", "adblock"])

# Home Page
startpage = str(config.configdir / 'startpage/index.html')
c.url.default_page = startpage
c.url.start_pages = startpage
c.url.searchengines = {"DEFAULT": "https://searx.be/?q={}"}

# Privacy
c.backend = "webengine"
c.qt.force_platform = "wayland"
c.content.proxy = 'system'

c.content.desktop_capture = False       # site permissions
c.content.mouse_lock = False
c.content.media.audio_capture = False
c.content.media.video_capture = False
c.content.media.audio_video_capture = False
c.content.geolocation = False
c.content.notifications.enabled = False
c.content.autoplay = False
c.content.canvas_reading = False
c.content.local_storage = False
c.content.persistent_storage = False
c.content.headers.do_not_track = True

c.content.cookies.accept = "no-3rdparty"
c.completion.cmd_history_max_items = 0
c.completion.web_history.max_items = 0
c.auto_save.session = False
c.content.blocking.method = "both"
c.content.blocking.enabled = True
c.content.cookies.store = False
c.content.headers.accept_language = "en-US,en;q=0.5"
c.content.headers.user_agent = "a potato running Google Chrome"
c.content.javascript.enabled = False
c.content.private_browsing = True
c.content.register_protocol_handler = False
c.content.webgl = False
c.content.webrtc_ip_handling_policy = "default-public-interface-only"
c.content.headers.referer = "same-domain"

# UI
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'smart'
c.colors.webpage.darkmode.policy.page = 'smart'
c.scrolling.smooth = True

c.completion.height = "20%"
c.completion.shrink = True
c.statusbar.show = 'in-mode'
c.statusbar.padding = {"bottom": 4, "left": 4, "right": 4, "top": 4}
c.tabs.padding = {"bottom": 3, "left": 5, "right": 5, "top": 3}
c.tabs.favicons.show = "never"
c.tabs.title.alignment = 'center'
c.tabs.title.format = "{audio}<{index}> {current_title}"
c.tabs.title.format_pinned = "<{index}>"

# coloring
c.colors.webpage.bg =                             "#121212"

c.colors.tabs.even.bg =                           "#2a2a2a"  # tabs
c.colors.tabs.odd.bg =                            "#2a2a2a"
c.colors.tabs.selected.even.bg =                  "#1a1a1a"
c.colors.tabs.selected.odd.bg =                   "#1a1a1a"

c.colors.statusbar.caret.fg =                     "#C678DD"
c.colors.statusbar.command.fg =                   "#E06C75"
c.colors.statusbar.command.private.fg =           "#E06C75"
c.colors.statusbar.insert.fg =                    "#98C379"
c.colors.statusbar.normal.fg =                    "#61AFEF"
c.colors.statusbar.private.fg =                   "#61AFEF"
c.colors.statusbar.command.bg =                   "#1a1a1a"
c.colors.statusbar.command.private.bg =           "#1a1a1a"
c.colors.statusbar.insert.bg =                    "#1a1a1a"
c.colors.statusbar.normal.bg =                    "#1a1a1a"
c.colors.statusbar.private.bg =                   "#1a1a1a"

c.colors.statusbar.url.fg =                       "#ffffff"  # urls
c.colors.statusbar.url.success.http.fg =          "#EA936C"
c.colors.statusbar.url.success.https.fg =         "#98C379"
c.colors.statusbar.url.hover.fg =                 "#61AFEF"

c.colors.completion.even.bg =                     "#1b1b1b"  # completion menu
c.colors.completion.odd.bg =                      "#1b1b1b"
c.colors.completion.category.bg =                 "#121212"
c.colors.completion.category.fg =                 "#61AFEF"
c.colors.completion.item.selected.bg =            "#E5C07B"
c.colors.completion.item.selected.border.top =    "#E5C07B"
c.colors.completion.item.selected.border.bottom = "#E5C07B"

# Binds & Aliases
config.bind(',m', 'spawn -d mpv {url}')
config.bind(',M', 'hint links spawn -d mpv {hint-url}')
config.bind(',n', 'spawn -u untrack-url -o {url}')
config.bind('gi', 'hint inputs')

config.unbind('=', mode='normal')  # zooming
config.unbind('+', mode='normal')
config.unbind('-', mode='normal')
config.bind('z=', 'zoom-in')
config.bind('z-', 'zoom-out')
config.bind('zz', 'zoom')

config.bind('tt', 'config-cycle -p content.proxy socks://localhost:9050/ system')

c.aliases = {
  'o': 'open',
  'q': 'quit',
  'so': 'config-source',
}

# QOL
c.confirm_quit = ["downloads"]
c.tabs.last_close = "startpage"
c.search.wrap = False
c.tabs.show = "multiple"

c.editor.command = ["foot", "-e", "nvim", "{}"]
