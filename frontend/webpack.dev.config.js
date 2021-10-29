const path = require('path');
const webpack = require("webpack");
const MiniCssExractPlugin = require('mini-css-extract-plugin');
const BundleTracker = require('webpack-bundle-tracker');
const StylelintPlugin = require('stylelint-webpack-plugin');
const CopyWebpackPlugin = require("copy-webpack-plugin");

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
            },
            {
                test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)(\?.*)?$/,
                use: {
                  loader: 'file-loader',
                  options: {
                    name: '[path][name].[ext]',
                  },
                },
            },
        ]
    },
    plugins: [
        new CopyWebpackPlugin({ 
            patterns: [{ 
                from: path.resolve(__dirname, './src/images'), to: '../images'
            }] 
        }),
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
        compress: true,
        liveReload: true,
        allowedHosts: 'auto',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'X-Requested-With, content-type, Authorization',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
        }
    }
};