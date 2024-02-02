import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import type { InsertionContext } from '@jupyter-ai/core';

/**
 * Initialization data for the jupyter-ai-chat extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyter-ai-chat:plugin',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension jupyter-ai-chat is activated!');

    // handles "test" insertion mode, which just shows output in a native
    // browser alert.
    app.commands.addCommand('ai:insert-test', {
      execute: ((context: InsertionContext) => {
        alert(context.response.output)
      }) as any
    })
  }
};

export default plugin;
