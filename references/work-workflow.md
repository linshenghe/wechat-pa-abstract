# ChatGPT Work / Codex Routing

Use this reference when the task is started in ChatGPT Work, when the execution location is unclear, or when the task may resume after an interruption.

## Capability routing

Do not infer Office capability from the product label alone. Confirm the actual execution location and available tools:

- **Local Work:** runs through the desktop app and may access approved local files and applications.
- **Codex Local/Worktree:** runs on the computer; Worktree additionally isolates project changes.
- **Cloud Work or Codex Cloud:** runs remotely. It may work with supplied or uploaded files, but it cannot directly open the user's local Word or PowerPoint.

Computer-use access, application approval, and the target Office installation must still be available in a local run. If they are not, treat the Office gate as unavailable rather than retrying with unrelated tools.

## Deliverable levels

Select the lightest level that satisfies the request:

1. **Chat text:** use when the user asks for text only, a quick translation, or a draft with no file.
2. **Reviewable package:** create the bilingual manuscript and requested files, but label visual validation as pending when local Office cannot be used.
3. **Final package:** deliver the Word manuscript and cover only after the required PowerPoint and Word visual checks plus the deterministic final check pass.

The skill's default for an ordinary short or long summary remains the Word-plus-cover package. An explicit text-only, draft-only, or no-Word request overrides that default.

## Efficient Work execution

- Resolve the project output root from project instructions and the skill bundle root from the loaded skill independently. Pass absolute paths to the template and bundled scripts.
- Reuse a valid task-local intermediate or final artifact when its source and inputs are unchanged. Do not rebuild a cover or manuscript merely because the Work conversation resumed.
- Perform content and source checks before opening Office. This avoids spending a Work interaction on a missing-field or incomplete-source blocker.
- In a local run, keep the Office phase short and isolated. Ask the user not to manipulate the target Office window only during the opening, permission, screenshot, metrics, and close sequence.
- In a cloud run, do not try local application commands. Complete the non-Office work if useful, then report the exact missing visual gate and the smallest way to continue locally.
- Report only meaningful milestones: content ready, files built, and final status. Keep raw command output and QA intermediates out of the handoff unless requested.

## External actions

The English delivery email is a draft in chat. Do not send, upload, share, publish, or overwrite an existing manuscript unless the user explicitly requests and authorizes that action.
