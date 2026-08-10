on replaceText(findText, replacementText, sourceText)
    set savedDelimiters to AppleScript's text item delimiters
    set AppleScript's text item delimiters to findText
    set textItems to every text item of sourceText
    set AppleScript's text item delimiters to replacementText
    set replacedText to textItems as text
    set AppleScript's text item delimiters to savedDelimiters
    return replacedText
end replaceText

on run argv
    if (count of argv) is not 2 then error "Usage: write_cover_title.applescript <pptx-path> <uppercased-title>" number 64

    set pptPath to item 1 of argv
    set desiredTitle to item 2 of argv
    set softBreak to ASCII character 11
    repeat while desiredTitle contains ": "
        set desiredTitle to my replaceText(": ", ":", desiredTitle)
    end repeat
    repeat while desiredTitle contains "; "
        set desiredTitle to my replaceText("; ", ";", desiredTitle)
    end repeat
    repeat while desiredTitle contains "： "
        set desiredTitle to my replaceText("： ", "：", desiredTitle)
    end repeat
    repeat while desiredTitle contains "； "
        set desiredTitle to my replaceText("； ", "；", desiredTitle)
    end repeat
    set desiredTitle to my replaceText(":", ":" & softBreak, desiredTitle)
    set desiredTitle to my replaceText(";", ";" & softBreak, desiredTitle)
    set desiredTitle to my replaceText("：", "：" & softBreak, desiredTitle)
    set desiredTitle to my replaceText("；", "；" & softBreak, desiredTitle)

    with timeout of 45 seconds
        tell application "Microsoft PowerPoint"
            activate
            open POSIX file pptPath
            repeat 40 times
                if (count of presentations) > 0 then exit repeat
                delay 0.25
            end repeat
            if (count of presentations) is 0 then error "PowerPoint did not open the presentation" number 65

            set workingPresentation to active presentation
            set titleRange to text range of text frame of shape "Title 1" of slide 1 of workingPresentation
            set content of titleRange to desiredTitle
            save workingPresentation
            set verifiedTitle to content of text range of text frame of shape "Title 1" of slide 1 of workingPresentation
            if verifiedTitle does not equal desiredTitle then error "PowerPoint title read-back mismatch" number 66
            return verifiedTitle
        end tell
    end timeout
end run
