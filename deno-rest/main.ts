import { Application, Router } from "https://deno.land/x/oak@v7.3.0/mod.ts";

const router = new Router();
router.get("/fibonacci/v1/sequence/:order", (context: any) => {
    const order = parseInt(context.params.order);
    const f = [0, 1];
    for (let i = 2, l = order; i <= l; i++) {
        f.push(f[i - 1] + f[i - 2]);
    }
    context.response.headers.set("Content-Type", "application/json")
    context.response.status = 200;
    context.response.body = {
        data: {
            value: f[order]
        }
    };
});

const app = new Application();
app.use(router.routes());
app.use(router.allowedMethods());

await app.listen({ port: 8000 });
