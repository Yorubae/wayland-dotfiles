if status is-interactive
    # Commands to run in interactive sessions can go here
	#set -U fish_greeting "Yoru's shell~"
	function fish_greeting
		fortune -a
	end
end

