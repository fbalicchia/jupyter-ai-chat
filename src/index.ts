import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

/**
 * Initialization data for the jupyter-ai-chat extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyter-ai-chat:plugin',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension jupyter-ai-chat is activated!');

  }
};

export default plugin;
