const path = require('path');
const webpack = require("webpack");
const MiniCssExractPlugin = require('mini-css-extract-plugin');
const BundleTracker = require('webpack-bundle-tracker');
const StylelintPlugin = require('stylelint-webpack-plugin');

module.exports = {
    entry: './src/js/index.js',
    mode: 'development',
    output: {
        filename: 'scripts.bundle.js',
        path: path.join(__dirname, '../static/js'),
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
                options: {
                    cacheDirectory: true,
                    presets: [
                        [
                            '@babel/preset-env',
                            {
                                'targets': 'defaults'
                            }
                        ]
                    ],
                },
              },
            {
                test: /\.(s)css$/,
                use: [
                    MiniCssExractPlugin.loader,
                    'css-loader', 
                    'postcss-loader', 
                    'sass-loader', 
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExractPlugin({
            filename: '../css/styles.bundle.css',
        }),
        new BundleTracker({
            filename: './webpack-stats.json',
        }),
        new webpack.HotModuleReplacementPlugin(),
        new StylelintPlugin(),
    ],
    devServer: {
        port: 3000,
        hotOnly: true,
        writeToDisk: true,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'X-Requested-With, content-type, Authorization',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
        }
    }
};