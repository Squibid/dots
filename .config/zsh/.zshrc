#~/.zshrc

# opts
setopt autocd
setopt transientrprompt
setopt PROMPT_SUBST
setopt NO_CASE_GLOB
setopt SHARE_HISTORY
setopt APPEND_HISTORY
setopt INC_APPEND_HISTORY
setopt HIST_IGNORE_DUPS
setopt HIST_REDUCE_BLANKS
stty stop undef

# completion menu
zstyle ':completion:*' menu select
zmodload zsh/complist
autoload -U compinit && compinit -u
# auto complete with case insensitivity
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'
# auto complete with privilaged commands
zstyle ':completion::complete:*' gain-privileges 1

# vim mode
bindkey -v
export KEYTIMEOUT=1

# Use vim keys in tab complete menu:
bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'j' vi-down-line-or-history
bindkey -M menuselect 'Tab' forward-menu-complete
bindkey -M menuselect '^[[Z' reverse-menu-complete # shift tab for backwards menu completion
# Fix backspace bug when switching modes
bindkey "^?" backward-delete-char

# Change cursor shape for different vi modes.
function zle-keymap-select {
  if [[ ${KEYMAP} == vicmd ]] ||
    [[ $1 = 'block' ]]; then
    echo -ne '\e[1 q'
  elif [[ ${KEYMAP} == main ]] ||
    [[ ${KEYMAP} == viins ]] ||
    [[ ${KEYMAP} = '' ]] ||
    [[ $1 = 'beam' ]]; then
    echo -ne '\e[5 q'
  fi
}
zle -N zle-keymap-select

zle-line-init() {
  zle -K viins # initiate `vi insert` as keymap (can be removed if `bindkey -V` has been set elsewhere)
  echo -ne "\e[5 q"
}
zle -N zle-line-init

# prompt
if [ ~ = "/root" ]; then
  symbol="#"
else
  symbol="$"
fi
PROMPT="%B%F{5}[%n@%m %c]$symbol%f%b "
RPROMPT="%(?.%F{2}┳━┳ ノ(•_•ノ)%f.%F{1}(╯°□°%)╯︵ ┻━┻%f)"

# muh shell agnostic stuff
source "${XDG_CONFIG_HOME:-$HOME/.config}/shell/aliasrc"
source "${XDG_CONFIG_HOME:-$HOME/.config}/shell/profile"
